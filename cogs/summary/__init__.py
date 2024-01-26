import os

from nextcord.ext import commands
import nextcord
from openai import OpenAI
from loguru import logger as log
from sqlmodel import Session, select

from db import new_engine
from db.models import Request, SummaryReplies, Feedback
from db.helpers import process_request
from utils import get_youtube_video_id
from cogs.summary.summary import process_summary
from utils.webhooks import send_error_webhook

used_emojis = ['📖', '👎', '👍']


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

        self.engine = new_engine()
        _, request, _ = process_request(
            self.engine, message, message.content, 'summary', 'normal')
        async with message.channel.typing():
            with Session(self.engine) as session:
                try:
                    _, _ = process_summary(
                        session, self.openai, videoId, request)
                    await message.add_reaction('📖')
                except Exception as e:
                    error_message = str(e)
                    # send an error log, but don't reply to the message
                    await send_error_webhook(error_message, 'summary', message.channel.id, message.id,
                                             message.author.id, message.content)
                    log.error(f"Error getting transcript: {error_message}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: nextcord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return
        if payload.emoji.name not in used_emojis:
            return
        self.engine = new_engine()
        if payload.emoji.name == '📖':
            channel = self.bot.get_channel(payload.channel_id)
            async with channel.typing():
                with Session(self.engine) as session:
                    statement = select(SummaryReplies).where(
                        SummaryReplies.original_message_id == str(payload.message_id))
                    summary_reply = session.exec(statement).first()
                    if summary_reply is not None:
                        return
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
                    reply = await self.reply_with_summary(payload.channel_id, payload.message_id, content)
                    await reply.add_reaction('👍')
                    await reply.add_reaction('👎')
                    summary_reply = SummaryReplies(
                        original_message_id=str(payload.message_id),
                        reply_message_id=str(reply.id),
                        summary_id=summary.id)
                    session.add(summary_reply)
                    session.commit()
        # need to add a method to make sure there's no duplicates
        elif payload.emoji.name == '👎':
            # add to feedback
            channel = self.bot.get_channel(payload.channel_id)
            # user doesn't need to know that we're typing
            with Session(self.engine) as session:
                statement = select(SummaryReplies).where(
                    SummaryReplies.reply_message_id == str(payload.message_id))
                summary_reply = session.exec(statement).first()
                if summary_reply is None:
                    return
                summary = summary_reply.summary
                feedback = Feedback(
                    request_id=summary.req_id,
                    summary_id=summary.id,
                    feedback='negative',
                    rating=-1
                )
                session.add(feedback)
                session.commit()
                log.info(
                    f"Added {feedback.feedback} feedback for {summary.id}")
        elif payload.emoji.name == '👍':
            # add to feedback
            channel = self.bot.get_channel(payload.channel_id)
            # user doesn't need to know that we're typing
            with Session(self.engine) as session:
                statement = select(SummaryReplies).where(
                    SummaryReplies.reply_message_id == str(payload.message_id))
                summary_reply = session.exec(statement).first()
                if summary_reply is None:
                    return
                summary = summary_reply.summary
                feedback = Feedback(
                    request_id=summary.req_id,
                    summary_id=summary.id,
                    feedback='positive',
                    rating=1
                )
                session.add(feedback)
                session.commit()
                log.info(
                    f"Added {feedback.feedback} feedback for {summary.id}")

    async def reply_with_summary(self, channel_id: int, message_id: int, content: str):
        channel = self.bot.get_channel(channel_id)
        if not channel:
            return
        message = await channel.fetch_message(message_id)
        if not message:
            return
        m = await message.reply(content)
        return m


def setup(bot):
    bot.add_cog(SummaryCog(bot))
