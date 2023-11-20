import os

from nextcord.ext import commands
import nextcord
from openai import OpenAI
from loguru import logger as log
from sqlmodel import Session, select

from db import new_engine
from db.models import Request
from db.helpers import process_request
from utils import get_youtube_video_id
from cogs.summary.summary import process_summary


class SummaryCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        log.info("Loaded SummaryCog")

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if not ('youtube.com' in message.content or 'youtu.be' in message.content):
            return

        # if its in a message thread, ignore it
        if message.channel.type == nextcord.ChannelType.private_thread or message.channel.type == nextcord.ChannelType.public_thread:
            return

        if message.author.bot or message.author.id == self.bot.user.id:
            return

        videoId = get_youtube_video_id(message.content)
        if not videoId:
            return

        _, request, _ = process_request(
            self.engine, message, message.content, 'summary', '')
        async with message.channel.typing():
            with Session(self.engine) as session:
                try:
                    _, _ = process_summary(
                        session, self.openai, videoId, request)
                    await message.add_reaction('📖')
                except Exception as e:
                    error_message = str(e)
                    # send an error log, but don't reply to the message
                    log.error(f"Error getting transcript: {error_message}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: nextcord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return
        if payload.emoji.name != '📖':
            return
        async with self.bot.get_channel(payload.channel_id).typing():
            has_replied = await self.has_bot_replied(payload.channel_id, payload.message_id)
            if has_replied:
                return
            with Session(self.engine) as session:
                statement = select(Request).where(
                    Request.message_id == str(payload.message_id))
                request = session.exec(statement).first()
                if request is None:
                    return
                summary, _ = process_summary(
                    session, self.openai, get_youtube_video_id(request.prompt), request)
                content = f'Here\'s your summary!\n\n{summary.summary}'
                if len(content) > 2000:
                    content = content[:1997] + '...'
                await self.reply_with_summary(payload.channel_id, payload.message_id, content)

    async def reply_with_summary(self, channel_id: int, message_id: int, content: str):
        channel = self.bot.get_channel(channel_id)
        if not channel:
            return
        message = await channel.fetch_message(message_id)
        if not message:
            return
        await message.reply(content)

    async def has_bot_replied(self, channel_id, message_id):
        """
        Checks if the bot has already replied to a specific message in a Discord channel.

        :param channel_id: ID of the Discord channel
        :param message_id: ID of the message to check
        :return: True if the bot has replied, False otherwise
        """
        # Fetch the channel
        channel = self.bot.get_channel(channel_id)
        if not channel:
            print(f"Channel with ID {channel_id} not found.")
            return False

        # Fetch recent messages in the channel
        try:
            messages = await channel.history(limit=100).flatten()
        except Exception as e:
            print(f"Error fetching messages: {e}")
            return False

        # Check for bot's reply among recent messages
        for msg in messages:
            if msg.reference and msg.reference.message_id == message_id and msg.author == self.bot.user:
                return True

        return False


def setup(bot):
    bot.add_cog(SummaryCog(bot))
