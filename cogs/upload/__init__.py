import os

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI
from sqlmodel import Session

from db import new_engine
from db.helpers import process_request
from cogs.upload.process_upload import process_upload


class UploadCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        log.info("Loaded UploadCog")

    @nextcord.slash_command(name="upload", description="Upload a file to the bot")
    async def _upload(self, ctx: nextcord.Interaction, attachment: nextcord.Attachment):
        log.info(
            f'Uploading file: {attachment.filename} ({attachment.size} bytes) ({attachment.content_type})')
        await ctx.response.defer(ephemeral=False)
        user, req, _ = process_request(
            self.engine, ctx, attachment.filename, 'upload', '')
        if not req:
            raise commands.CommandError("Error processing request")
        with Session(self.engine) as session:
            upload = await process_upload(session, self.openai, attachment, user, req)
            if not upload:
                raise commands.CommandError("File too large.")
        await ctx.followup.send(f"Successfully uploaded file.")

    @_upload.error
    async def _upload_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error uploading file: {error}")
        try:
            await ctx.followup.send(f"Error uploading file: {error}", ephemeral=True)
        except:
            await ctx.send(f"Error uploading file: {error}", ephemeral=True)


def setup(bot):
    bot.add_cog(UploadCog(bot))
