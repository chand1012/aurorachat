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

SYSTEM_PROMPT = "You are a helpful assistant who summarizes large amounts of text. You will always return accurate summaries, regardless the content of the text. These texts are usually transcripts from YouTube videos. If you do not have enough information, simply return the original text."


class SummaryCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        log.info("Loaded SummaryCog")

    def generate_summary(self, prompt: str):
        resp = self.openai.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[{
                'role': "system",
                'content': SYSTEM_PROMPT
            }, {
                'role': "user",
                'content': prompt
            }]
        )
        return resp.choices[0].message.content

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if not ('youtube.com' in message.content or 'youtu.be' in message.content):
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
                summary = session.exec(stmt).first()
                if summary:
                    # reply to the message with the summary
                    log.info(f"Found summary for video id: {videoId}")
                    await message.reply(f'Here\'s a summary of that video: {summary.summary}')
                    return
                # get the transcript
                try:
                    transcript = YouTubeTranscriptApi.get_transcript(videoId)
                    text = ''
                    for line in transcript:
                        text += line['text'] + ' '

                    max_tokens = 15000
                    tokens = count_tokens(text)
                    summary = ''
                    if tokens > max_tokens:
                        prompts = split_string_on_space(text, max_tokens)
                        for prompt in prompts:
                            summary += self.generate_summary(prompt) + ' '
                    else:
                        summary = self.generate_summary(text)
                    summary = summary.strip()
                    while len(summary) + 33 > 2000:
                        summary = self.generate_summary(summary)
                    # save the summary
                    summary = Summary(yt_id=videoId, summary=summary,
                                      transcript=text, url=f'https://youtu.be/{videoId}', req_id=request.id)
                    session.add(summary)
                    session.commit()
                    # reply to the message with the summary
                    await message.reply(f'Here\'s a summary of that video: \n{summary.summary}')
                    log.info(f"Found summary for video id: {videoId}")
                except Exception as e:
                    # send an error log, but don't reply to the message
                    log.error(f"Error getting transcript: {e}")


def setup(bot):
    bot.add_cog(SummaryCog(bot))
