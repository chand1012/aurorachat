import os


from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI
from sqlmodel import Session, select
import humanize

from utils import truncate_string, process_audio
from db import new_engine
from db.models import Thread, Overrides
from db.helpers import process_request, process_text_response
from utils.upload import process_upload, process_audio, AUDIO_FILE_EXT
from cogs.chat.process_thread import process_thread
from utils.webhooks import send_error_webhook


class ChatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        log.info("Loaded ChatCog")

    @nextcord.slash_command(name="chat", description="DEPRECATED. Please either start a new thread and tag her or simply mention her in a message.")
    async def _chat(self, ctx: nextcord.Interaction):
        await ctx.send("This command is deprecated. Please either start a new thread and tag Aurora or simply mention her in a message.", ephemeral=True)


def setup(bot):
    bot.add_cog(ChatCog(bot))
