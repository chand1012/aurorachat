# the cleaner takes old threads and cleans them up
import os
import asyncio
from datetime import datetime, timedelta

from nextcord.ext import commands, tasks
import nextcord
from loguru import logger as log
from openai import OpenAI
from sqlmodel import Session, select

from db import new_engine
from db.models import Request
from utils.webhooks import send_error_webhook


class CleanerCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        self.lock = asyncio.Lock()
        log.info("Loaded CleanerCog")
        self.cleaner.start()
        self.first_run = False

    def cog_unload(self):
        self.cleaner.cancel()

    @tasks.loop(hours=12)
    async def cleaner(self):
        if not self.first_run:
            log.info("Skipping first run.")
            self.first_run = True
            return
        async with self.lock:
            try:
                log.info("Running cleaner")
                self.engine = new_engine()
                with Session(self.engine) as session:
                    # get all requests in the last 24 hours that have a thread
                    requests = session.exec(select(Request).where(
                        Request.created_at > datetime.now() - timedelta(days=7))).all()
                    threads = []
                    for req in requests:
                        threads += req.thread
                    log.info(f'Found {len(threads)} threads to clean')
                    for thread in threads:
                        try:
                            # get the channel
                            channel: nextcord.Thread = self.bot.get_channel(
                                int(thread.discord_id))
                            if not channel:
                                continue
                            await channel.edit(locked=True, archived=True)
                            self.openai.beta.threads.delete(
                                thread_id=thread.openai_id)
                            session.delete(thread)
                            session.commit()
                        except Exception as e:
                            log.error(f'Error cleaning thread: {e}')
                log.info("Finished cleaning")
            except Exception as e:
                log.error(f'Error cleaning: {e}')
                await send_error_webhook(str(e), 'cleaner', '', '', '', '')

    @cleaner.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()


def setup(bot: commands.Bot):
    bot.add_cog(CleanerCog(bot))
