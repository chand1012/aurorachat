import os

from nextcord.ext import commands
import nextcord
from openai import OpenAI
from loguru import logger as log
from sqlmodel import Session, select
from youtube_transcript_api import YouTubeTranscriptApi

from ai import count_tokens
from db import new_engine
from db.models import Summary
from db.helpers import process_request
from utils import get_youtube_video_id, split_string_on_space
from cogs.summary.summary import summarize


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
                stmt = select(Summary).where(Summary.yt_id == videoId)
                s = session.exec(stmt).first()
                if s:
                    # reply to the message with the summary
                    log.info(f"Found summary for video id: {videoId}")
                    await message.reply(f'Here\'s a summary of that video: {s.summary}')
                    return
                # get the transcript
                try:
                    transcript, summary = summarize(self.openai, videoId)
                    # save the summary
                    s = Summary(yt_id=videoId, summary=summary,
                                transcript=transcript, url=f'https://youtu.be/{videoId}', req_id=request.id)
                    session.add(s)
                    session.commit()
                    # reply to the message with the summary
                    await message.reply(f'Here\'s a summary of that video: \n{s.summary}')
                    log.info(f"Found summary for video id: {videoId}")
                except Exception as e:
                    error_message = str(e)
                    if len(error_message) > 1800:
                        error_message = error_message[:1800]
                    # send an error log, but don't reply to the message
                    log.error(f"Error getting transcript: {error_message}")


def setup(bot):
    bot.add_cog(SummaryCog(bot))
