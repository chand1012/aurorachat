import os

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from sqlmodel import Session, select
import humanize
from openai import OpenAI

from athenadb import AthenaDB
from db import new_engine
from db.models import Overrides
from db.helpers import process_request, process_text_response
from utils.webhooks import send_error_webhook


class QuickChatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.engine = new_engine()
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.athena = AthenaDB(os.getenv('ATHENA_DB'))
        log.info("Loaded QuickChatCog")

    # listen for messages
    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author == self.bot.user:
            return
        # the message has to mention the bot
        if not message.mentions or message.mentions[0] != self.bot.user:
            return

        try:
            async with message.channel.typing():
                self.engine = new_engine()
                # this returns things. We don't care until we want to start rate limiting
                _, req, time_remaining = process_request(self.engine, message,
                                                         message.content, 'text', 'free')
                if time_remaining is not None:
                    await message.channel.send(f"Sorry, you've reached the free limit for today. Please try again in {humanize.precisedelta(time_remaining, minimum_unit='minutes')}", reference=message)
                    return
                system_prompt = 'You are a helpful Discord assistant named Aurora. You will always be polite and helpful. Use any given information above to help answer the user\'s question.'
                athena_namespace = None
                # check if an override exists
                with Session(self.engine) as session:
                    statement = select(Overrides).where(
                        Overrides.guild_id == str(message.guild.id))
                    override = session.exec(statement).first()
                    if override:
                        if override.quickchat_system_prompt:
                            system_prompt = override.quickchat_system_prompt
                        if override.athena_namespace:
                            athena_namespace = override.athena_namespace

                if athena_namespace is not None:
                    system_prompt += " Only use the given information to answer the question. If the answer to their question is not in the given information, tell them that you are not sure or don't know."

                context = [{
                    'content': system_prompt,
                    'role': 'system'
                }]

                # if the message is a reply, we don't want to respond to it.
                # Eventually she'll treat it as a simple message thread, but for now
                # we should just ignore it so that the feedback loop doesn't happen
                if message.reference:
                    reference = message.reference
                    while reference and len(context) < 10:
                        current_message = await message.channel.fetch_message(reference.message_id)
                        if not current_message:
                            return
                        if 'conversation is getting a bit long' in current_message.content:
                            return
                        context.append({
                            'content': current_message.content,
                            'role': 'assistant' if current_message.author == self.bot.user else 'user'
                        })
                        if current_message.interaction:
                            if current_message.interaction.type == 2:
                                return
                        if current_message.reference:
                            reference = current_message.reference
                        else:
                            break
                log.info(
                    f'QuickChat from {message.author} on {message.channel.id}: {message.content}')
                prompt = message.content
                # remove the mention from the prompt
                prompt = prompt.replace(f'<@{self.bot.user.id}>', '')
                prompt = prompt.strip()

                if athena_namespace is not None:
                    if len(prompt) > 1000:
                        prompt = prompt[:1000]
                    resp: dict = await self.athena.query(input=prompt, namespace=athena_namespace)
                    vectors = resp.get('vectors')
                    if vectors:
                        information = '\n'.join(v['text'] for v in vectors)
                        p = context[0]['content']
                        context[0]['content'] = f'{information}\n\n{p}'
                context.append({
                    'content': prompt,
                    'role': 'user'
                })

                response = self.openai.chat.completions.create(
                    messages=context,
                    model='gpt-4o-mini',
                )
                text = response.choices[0].message.content
                with Session(self.engine) as session:
                    process_text_response(session, req, text)
                log.info(
                    f'QuickChat response to {message.author} on {message.channel.id}: {text}')

                if len(text) > 2000:
                    # chunk the message
                    chunks = [text[i:i+2000]
                              for i in range(0, len(text), 2000)]
                    for chunk in chunks:
                        await message.channel.send(chunk, reference=message)
                else:
                    # for now just echo the prompt back and print to the console
                    await message.channel.send(text, reference=message)
        except Exception as e:
            log.error(e)
            # await send_error_webhook(str(e), str(message.channel.id), str(message.id), str(message.author.id), str(message.content))
            await message.channel.send("Sorry, I'm having trouble understanding you. Please try again later.", reference=message)
            await send_error_webhook(str(e), 'quickchat', str(message.channel.id), str(message.id), str(message.author.id), str(message.content))


def setup(bot: commands.Bot):
    bot.add_cog(QuickChatCog(bot))
