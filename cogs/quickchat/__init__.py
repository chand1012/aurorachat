import os

from nextcord.ext import commands
import nextcord
from loguru import logger as log
# from sqlmodel import Session, select


from ai import WorkersAILLMClient
from db import new_engine
# from db.models import Request
from db.helpers import process_request

# this will be free for all users for the foreseeable future


class QuickChatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.engine = new_engine()
        self.ai = WorkersAILLMClient()
        log.info("Loaded QuickChatCog")

    # listen for messages
    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author == self.bot.user:
            return
        # the message has to mention the bot
        if not message.mentions or message.mentions[0] != self.bot.user:
            return

        # the message has to be in a regular channel. Not a DM, not a thread, not a group DM
        if not isinstance(message.channel, nextcord.TextChannel):
            return

        async with message.channel.typing():
            # this returns things. We don't care until we want to start rate limiting
            process_request(self.engine, message,
                            message.content, 'text', 'free')
            context = []
            # if the message is a reply, we don't want to respond to it.
            # Eventually she'll treat it as a simple message thread, but for now
            # we should just ignore it so that the feedback loop doesn't happen
            if message.reference:
                reference = message.reference
                while reference and len(context) < 6:
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
            if len(context) > 6:
                log.warning(
                    f'User {message.author} has a long message thread.')
                await message.channel.send("This conversation is getting a bit long, so I'm going to stop here. If you want to have longer conversations with me, please use the `/chat` command.", reference=message)
                return
            prompt = message.content
            # remove the mention from the prompt
            prompt = prompt.replace(f'<@{self.bot.user.id}>', 'Aurora,')
            prompt = prompt.strip()
            # _, _, allowed = process_request(
            #     self.engine, message, prompt, 'text', 'free')
            context.append({
                'content': prompt,
                'role': 'user'
            })
            context = self.ai.truncate_conversation(context)
            response = await self.ai.run(context)
            response = response.strip()
            log.info(
                f'QuickChat response to {message.author} on {message.channel.id}: {response}')
            # for now just echo the prompt back and print to the console
            await message.channel.send(response, reference=message)


def setup(bot: commands.Bot):
    bot.add_cog(QuickChatCog(bot))
