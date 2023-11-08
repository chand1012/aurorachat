import os
import asyncio

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI
from sqlmodel import Session, select

from utils import split_messages, truncate_string
from db import new_engine
from db.models import Thread
from db.helpers import process_request


async def process_thread(o: OpenAI, channel: nextcord.PartialMessageable, thread_id: str, assistant_id: str, content: str):
    o.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content
    )
    run = o.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
    )
    run_id = run.id
    status = run.status
    while status != "completed":
        run = o.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        status = run.status
        await asyncio.sleep(1)
    messages = o.beta.threads.messages.list(
        thread_id=thread_id,
    )
    # get the last message
    m = messages.data[0]
    content = m.content[0]
    response_text = content.text.value
    if len(response_text) > 2000:
        # split until the message is less than 2000 characters
        responses = split_messages(response_text)
        for response in responses:
            await channel.send(response)
    else:
        await channel.send(response_text)


class ChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        log.info("Loaded ChatCog")

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author == self.bot.user:
            return

        if message.channel.type == nextcord.ChannelType.public_thread or message.channel.type == nextcord.ChannelType.private_thread:
            # check if the bot is the one who started the thread
            if message.channel.owner != self.bot.user:
                return
            log.info(
                f'Received message in thread on {message.guild.name} ({message.guild.id})')
            async with message.channel.typing():
                prompt = message.content
                _, _, allowed = process_request(
                    self.engine, message, prompt, 'text', 'normal')
                if not allowed:
                    await message.channel.send("You have reached your request limit now. Please try again in a few hours.")
                    return
                thread_id = None
                assistant_id = None
                with Session(self.engine) as session:
                    statement = select(Thread).where(
                        Thread.discord_id == str(message.channel.id))
                    db_thread = session.exec(statement).first()
                    if db_thread is None:
                        log.error(
                            f"Error getting thread with discord id {message.channel.id}")
                        return
                    thread_id = db_thread.openai_id
                    assistant_id = db_thread.assistant_id

                await process_thread(self.openai, message.channel, thread_id, assistant_id, prompt)

    @nextcord.slash_command(name="chat", description="Chat with the bot")
    async def _chat(self, ctx: nextcord.Interaction, prompt: str | None = nextcord.SlashOption(name="prompt", description="The initial message to send", required=False)):
        # add this back when we have more assistants
        # quality: str | None = nextcord.SlashOption(name="quality", description="Quality of conversation", choices=['normal', 'better', 'best'], required=False, default='normal)
        await ctx.response.defer(ephemeral=False)
        # eventually there will be more assistants with differing quality
        assistant = os.getenv('ASSISTANT_ID')
        log.info(
            f"Creating new thread with assistant ({assistant}) for on {ctx.guild.name} ({ctx.guild.id}. Initial message: '{prompt}')")
        # process the request
        _, request, allowed = process_request(
            self.engine, ctx, prompt, 'text', 'normal')
        if not allowed:
            await ctx.followup.send("You have reached your request limit. Please try again in a few hours.")
            return
        thread = self.openai.beta.threads.create()
        # create a new discord thread
        thread_name = f"{truncate_string(prompt) if prompt else 'New Chat'}"
        thread_channel = await ctx.channel.create_thread(name=thread_name, type=nextcord.ChannelType.public_thread)
        with Session(self.engine) as session:
            thread_db = Thread(
                request_id=request.id,
                openai_id=thread.id,
                discord_id=str(thread_channel.id),
                assistant_id=assistant
            )
            session.add(thread_db)
            session.commit()
        await ctx.followup.send(f"Created thread {thread_channel.mention}")
        if prompt is None:
            await thread_channel.send("Hello! I am Sam, your helpful assistant. How can I help you today?")
        else:
            with thread_channel.typing():
                await process_thread(self.openai, thread_channel, thread.id, assistant, prompt)

    @nextcord.slash_command(name="delete", description="Delete the thread. Does nothing if the bot is not the owner or if not in a thread.")
    async def _delete(self, ctx: nextcord.Interaction):
        if ctx.channel.type == nextcord.ChannelType.public_thread or ctx.channel.type == nextcord.ChannelType.private_thread:
            if ctx.channel.owner != self.bot.user:
                return
            await ctx.channel.delete()

    @_delete.error
    async def _delete_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error deleting thread: {error}")
        try:
            await ctx.followup.send(f"Error deleting thread: {error}", ephemeral=True)
        except:
            await ctx.send(f"Error deleting thread: {error}", ephemeral=True)

    @_chat.error
    async def _chat_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error starting chat: {error}")
        try:
            await ctx.followup.send(f"Error starting chat: {error}", ephemeral=True)
        except:
            await ctx.send(f"Error starting chat: {error}", ephemeral=True)


def setup(bot):
    bot.add_cog(ChatCog(bot))
