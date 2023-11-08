import os
import io
from datetime import datetime

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI
from sqlmodel import Session

from db import new_engine
from db.models import UserUploads
from db.helpers import process_request


class UploadCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        log.info("Loaded UploadCog")

    @nextcord.slash_command(name="upload", description="Upload an image to the bot")
    async def _upload(self, ctx: nextcord.Interaction, attachment: nextcord.Attachment):
        log.info(
            f'Uploading file: {attachment.filename} ({attachment.size} bytes) ({attachment.content_type})')
        await ctx.response.defer(ephemeral=False)
        # if its greater than 8mb, reject it
        # TODO move this logic into a function so we can call it elsewhere
        if attachment.size > 8000000:
            await ctx.response.send_message("File is too big. Max size: 8mb")
            return
        user, req, _ = process_request(
            self.engine, ctx, attachment.filename, 'upload', '')
        if not req:
            raise commands.CommandError("Error processing request")
        content = await attachment.read()
        buf = io.BytesIO(content)
        buf.seek(0)
        resp = self.openai.files.create(
            file=buf,
            purpose="assistants",
        )
        with Session(self.engine) as session:
            upload = UserUploads(
                user_id=user.id,
                req_id=req.id,
                content_type=attachment.content_type,
                openai_id=resp.id,
                created_at=datetime.fromtimestamp(resp.created_at)
            )
            session.add(upload)
            session.commit()
        await ctx.followup.send(f"Successfully uploaded file.")

    @_upload.error
    async def _upload_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error uploading image: {error}")
        try:
            await ctx.followup.send(f"Error uploading image: {error}", ephemeral=True)
        except:
            await ctx.send(f"Error uploading image: {error}", ephemeral=True)


def setup(bot):
    bot.add_cog(UploadCog(bot))
