import os

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI


class TTSCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        log.info("Loaded TTSCog")

    @nextcord.slash_command(name="speak", description="Have Sam speak for you!")
    async def _speak(self, ctx: nextcord.Interaction, prompt: str):
        log.info(f"Generating speech with prompt: {prompt}")
        await ctx.response.defer(ephemeral=False)
        resp = self.openai.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=prompt,
            response_format="mp3",
            speed=0.9
        )
        await ctx.followup.send(file=nextcord.File(resp.content, filename="sam.mp3"))
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
