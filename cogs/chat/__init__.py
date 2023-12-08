import os


from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI
from sqlmodel import Session, select

from utils import truncate_string, process_audio
from db import new_engine
from db.models import Thread
from db.helpers import process_request
from utils.upload import process_upload, process_audio, AUDIO_FILE_EXT
from cogs.chat.process_thread import process_thread


class ChatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
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
                user, request, allowed = process_request(
                    self.engine, message, prompt, 'text', 'normal')
                if not allowed:
                    await message.channel.send("You have reached your request limit now. Please try again in a few hours.")
                    return
                try:
                    with Session(self.engine) as session:
                        statement = select(Thread).where(
                            Thread.discord_id == str(message.channel.id))
                        db_thread = session.exec(statement).first()
                        if db_thread is None:
                            log.error(
                                f"Error getting thread with discord id {message.channel.id}")
                            await message.channel.send("Sorry, I don't recognize this thread. Please start a new thread if you want to chat!")
                            return
                        # check to see if there are any attachments
                        files = []
                        if len(message.attachments) > 1:
                            raise commands.CommandError(
                                "You can only upload one file at a time for now.")
                        if len(message.attachments) > 0:
                            for attachment in message.attachments:
                                upload = None
                                if attachment.filename.endswith(tuple(AUDIO_FILE_EXT)):
                                    log.info(
                                        f"Got audio file {attachment.filename}. Transcribing and uploading...")
                                    upload = await process_audio(session, self.openai, attachment, user, request)
                                else:
                                    log.info(
                                        f"Got file {attachment.filename}. Uploading...")
                                    upload = await process_upload(session, self.openai, attachment, user, request)
                                if not upload:
                                    raise commands.CommandError(
                                        "File too large.")
                                files.append(upload.openai_id)

                        await process_thread(session, self.openai, message.channel, db_thread, request, files)
                except Exception as e:
                    log.error(f"Error processing thread: {e}")
                    await message.channel.send(f"Sorry! I had a problem with your request. {e}")
                    return

    @nextcord.slash_command(name="chat", description="Chat with Aurora. You can upload a file and/or provide a prompt.")
    async def _chat(self, ctx: nextcord.Interaction, prompt: str | None = nextcord.SlashOption(name="prompt", description="The initial message to send", required=False), attachment: nextcord.Attachment | None = nextcord.SlashOption(name="attachment", description="A file to upload", required=False)):
        # add this back when we have more assistants
        # quality: str | None = nextcord.SlashOption(name="quality", description="Quality of conversation", choices=['normal', 'better', 'best'], required=False, default='normal)
        await ctx.response.defer(ephemeral=False)
        if attachment and not prompt:
            await ctx.followup.send("You must provide a prompt if you are uploading a file.", ephemeral=True)
        # eventually there will be more assistants with differing quality
        assistant = os.getenv('ASSISTANT_ID')
        log.info(
            f"Creating new thread with assistant ({assistant}) for on {ctx.guild.name} ({ctx.guild.id}. Initial message: '{prompt}')")
        # process the request
        user, request, allowed = process_request(
            self.engine, ctx, prompt, 'text', 'normal')
        if not allowed:
            await ctx.followup.send("You have reached your request limit. Please try again in a few hours.")
            return
        if not request:
            raise commands.CommandError("Error processing request")
        upload = None
        files = []
        with Session(self.engine) as session:
            if attachment:
                upload = await process_upload(session, self.openai, attachment, user, request)
                if not upload:
                    raise commands.CommandError("File too large.")
                files.append(upload.openai_id)
            thread = self.openai.beta.threads.create()
            # create a new discord thread
            thread_name = f"{truncate_string(prompt) if prompt else 'New Chat'}"
            thread_channel = await ctx.channel.create_thread(name=thread_name, type=nextcord.ChannelType.public_thread)
            db_thread = Thread(
                request_id=request.id,
                openai_id=thread.id,
                discord_id=str(thread_channel.id),
                assistant_id=assistant
            )
            session.add(db_thread)
            session.commit()
            session.refresh(db_thread)
            await ctx.followup.send(f"Created thread {thread_channel.mention}")
            if prompt is None:
                await thread_channel.send("Hello! I am Sam, your helpful assistant. How can I help you today?")
            else:
                with thread_channel.typing():
                    await process_thread(session, self.openai, thread_channel, db_thread, request, files)

    @_chat.error
    async def _chat_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error starting chat: {error}")
        try:
            await ctx.followup.send(f"Error starting chat: {error}", ephemeral=True)
        except:
            await ctx.send(f"Error starting chat: {error}", ephemeral=True)

    @nextcord.slash_command(name="cancel", description="Cancels the current message. Does nothing if the bot is not the owner or if not in a thread.")
    async def _cancel(self, ctx: nextcord.Interaction):
        if ctx.channel.type == nextcord.ChannelType.public_thread or ctx.channel.type == nextcord.ChannelType.private_thread:
            if ctx.channel.owner != self.bot.user:
                return
            await ctx.response.defer(ephemeral=False)
            # get the current thread from the database
            with Session(self.engine) as session:
                statement = select(Thread).where(
                    Thread.discord_id == str(ctx.channel.id))
                db_thread = session.exec(statement).first()
                if db_thread is None:
                    raise commands.CommandError(
                        f"Error getting thread with discord id {ctx.channel.id}")
                # get the last run id and cancel it
                last_run_id = db_thread.last_run_id
                # get the current status of the run
                run = self.openai.beta.threads.runs.retrieve(
                    thread_id=db_thread.openai_id, run_id=last_run_id)
                match run.status:
                    case 'in_progress':
                        self.openai.beta.threads.runs.cancel(
                            thread_id=db_thread.openai_id, run_id=last_run_id)
                        await ctx.followup.send("Cancelled the current message.")
                    case 'queued':
                        await ctx.followup.send("Sorry, the current message is queued. Please wait a few seconds and try again.")
                    case _:
                        # TODO add contact info
                        await ctx.followup.send("Sorry, the current message cannot be cancelled. If this issue persists, please contact the bot owner.")

    @nextcord.slash_command(name="close", description="Closes a thread. Same as delete however it does not remove messages from discord.")
    async def _close_thread(self, ctx: nextcord.Interaction):
        if ctx.channel.type == nextcord.ChannelType.public_thread or ctx.channel.type == nextcord.ChannelType.private_thread:
            if ctx.channel.owner != self.bot.user:
                return
            await ctx.response.defer(ephemeral=False)
            with Session(self.engine) as session:
                statement = select(Thread).where(
                    Thread.discord_id == str(ctx.channel.id))
                db_thread = session.exec(statement).first()
                if db_thread is None:
                    raise commands.CommandError(
                        f"I cannot find this thread. Please start a new thread if you want to chat!")
                thread_id = db_thread.openai_id
                files = db_thread.request.useruploads
                for file in files:
                    self.openai.files.delete(file_id=file.openai_id)
                    # delete the file from the database
                    session.delete(file)
                self.openai.beta.threads.delete(thread_id=thread_id)
                session.delete(db_thread)
                session.commit()
                await ctx.followup.send("Closed the thread.")
                await ctx.channel.edit(locked=True, archived=True)

    @_close_thread.error
    async def _close_thread_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error closing thread: {error}")
        error_message = str(error)
        if len(error_message) > 1800:
            error_message = error_message[:1800]
        try:
            await ctx.followup.send(f"Error closing thread: {error_message}", ephemeral=True)
        except:
            await ctx.send(f"Error closing thread: {error_message}", ephemeral=True)

    @nextcord.slash_command(name="delete", description="Delete the thread. Does nothing if the bot is not the owner or if not in a thread.")
    async def _delete(self, ctx: nextcord.Interaction):
        if ctx.channel.type == nextcord.ChannelType.public_thread or ctx.channel.type == nextcord.ChannelType.private_thread:
            if ctx.channel.owner != self.bot.user:
                return
            with Session(self.engine) as session:
                statement = select(Thread).where(
                    Thread.discord_id == str(ctx.channel.id))
                db_thread = session.exec(statement).first()
                if db_thread is None:
                    raise commands.CommandError(
                        f"Error getting thread with discord id {ctx.channel.id}")
                thread_id = db_thread.openai_id
                files = db_thread.request.useruploads
                for file in files:
                    self.openai.files.delete(file_id=file.openai_id)
                    # delete the file from the database
                    session.delete(file)
                self.openai.beta.threads.delete(thread_id=thread_id)
                session.delete(db_thread)
                session.commit()
            await ctx.channel.delete()

    @_delete.error
    async def _delete_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error deleting thread: {error}")
        error_message = str(error)
        if len(error_message) > 1800:
            error_message = error_message[:1800]
        try:
            await ctx.followup.send(f"Error deleting thread: {error_message}", ephemeral=True)
        except:
            await ctx.channel.send(f"Error deleting thread: {error_message}", ephemeral=True)


def setup(bot):
    bot.add_cog(ChatCog(bot))
