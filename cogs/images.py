import os
import uuid
import io
import base64

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI

from sdxl import SDAPIAsync


class ImageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.sdxl = SDAPIAsync(base_url=os.getenv("SD_API_URL"))
        log.info("Loaded ImageCog")

    @nextcord.slash_command(name="imagine", description="Have Sam draw for you!")
    async def _imagine(self, interaction: nextcord.Interaction,
                       prompt: str, uncensored: str = nextcord.SlashOption(name="uncensored", description="Allow the image to be censored? Defaults to True. Requires 'best' quality and an NSFW channel.", required=False, choices=['false', 'true'], default='false'), quality: str | None = nextcord.SlashOption(name="quality", description="Image quality", required=False, choices=['normal', 'best'], default='normal')):
        log.info(
            f"Generating {quality} quality {'uncensored ' if uncensored == 'true' else ''} image with prompt: {prompt}")
        model = 'dall-e-2'
        if quality == 'best':
            model = 'dall-e-3'
        if uncensored == 'true':
            model = 'sdxl'
        await interaction.response.defer()
        if 'dall-e' in model:
            if len(prompt) > 1000 and model == 'dall-e-2':
                # truncate to the first 1000 characters
                prompt = prompt[:1000]
            resp = self.openai.images.generate(
                model=model,
                prompt=prompt,
                n=1,
                size="1024x1024",
                response_format="b64_json"
            )
            images = []
            image_data = resp.data
            for image in image_data:
                img = io.BytesIO(base64.b64decode(image.b64_json))
                img.seek(0)
                images.append(nextcord.File(
                    img, filename=f"{uuid.uuid4()}.jpg"))
            await interaction.followup.send(content=f"Full prompt: `{image.revised_prompt or prompt}`", files=images)
            log.info(
                f"Generated image with full prompt: {image.revised_prompt or prompt}")
        else:
            if not interaction.channel.is_nsfw() and uncensored == 'true':
                await interaction.followup.send("Cannot generate uncensored image in a non-NSFW channel.")
                return
            image = await self.sdxl.generate_image(prompt=prompt, width=1024, height=1024, negative_prompt=' watermark, disfigured, bad art, deformed, poorly drawn, extra limbs, close up, b&w, weird colors, blurry, depth of field, missing fingers, ugly face, extra legs')
            await interaction.followup.send(content=f"Full prompt: `{prompt}`", file=nextcord.File(image, filename=f"{uuid.uuid4()}.jpg"))

    @_imagine.error
    async def _imagine_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error generating image: {error}")
        try:
            await ctx.followup.send(f"Error generating image: {error}", ephemeral=True)
        except:
            await ctx.send(f"Error generating image: {error}", ephemeral=True)


def setup(bot):
    bot.add_cog(ImageCog(bot))
