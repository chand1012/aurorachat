import os

from nextcord.ext import commands
import nextcord
from openai import OpenAI
from loguru import logger as log
from sqlmodel import Session

from db import new_engine
from db.helpers import process_request
from utils import get_youtube_video_id
from cogs.summary.summary import process_summary


class SummaryCog(commands.Cog):
    def __init__(self, bot):
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
        async with message.channel.typing():
            log.info(f"Got video id: {videoId}")
            _, request, _ = process_request(
                self.engine, message, message.content, 'summary', '')
            # check if the summary exists
            with Session(self.engine) as session:
                # get the transcript
                try:
                    _, summary, cached = process_summary(
                        session, self.openai, videoId, request)
                    if cached:
                        # reply to the message with the summary
                        log.info(f"Found summary for video id: {videoId}")
                        await message.reply(f'Here\'s a summary of that video: {summary}')
                        return
                    await message.reply(f'Here\'s a summary of that video: {summary}')
                    # send the transcript as a file
                except Exception as e:
                    error_message = str(e)
                    if len(error_message) > 1800:
                        error_message = error_message[:1800]
                    # send an error log, but don't reply to the message
                    log.error(f"Error getting transcript: {error_message}")


def setup(bot):
    bot.add_cog(SummaryCog(bot))
