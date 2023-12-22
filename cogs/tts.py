import os
from io import BytesIO

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI
from sqlmodel import Session

from db import new_engine
from db.models import GeneratedFiles
from db.helpers import process_request


class TTSCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        log.info("Loaded TTSCog")

    @nextcord.slash_command(name="speak", description="Have Aurora speak for you!")
    async def _speak(self, ctx: nextcord.Interaction, prompt: str = nextcord.SlashOption(name="prompt", description="What you want me to say!"), speed: float = nextcord.SlashOption(name="speed", description="Speech speed", required=False, default=0.9, min_value=0.25, max_value=4.0)):
        log.info(f"Generating speech with prompt: {prompt}")
        _, request, _ = process_request(
            self.engine, ctx, prompt, 'speak', 'normal')
        await ctx.response.defer(ephemeral=False)
        resp = self.openai.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=prompt,
            response_format="mp3",
            speed=speed
        )
        b = BytesIO(resp.read())
        f = nextcord.File(b, filename="aurora.mp3")
        b.seek(0)
        size = b.getbuffer().nbytes
        await ctx.followup.send(file=f)
        with Session(self.engine) as session:
            session.add(GeneratedFiles(
                req_id=request.id,
                file_type='speech',
                size=size,
            ))
            session.commit()
        log.info(f"Generated speech with prompt: {prompt}")

    @_speak.error
    async def _speak_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error generating speech: {error}")
        try:
            await ctx.followup.send(f"Error generating speech: {error}", ephemeral=True)
        except:
            await ctx.send(f"Error generating speech: {error}", ephemeral=True)


def setup(bot):
    bot.add_cog(TTSCog(bot))
