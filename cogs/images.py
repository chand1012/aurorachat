import os
import uuid
import io
import base64
import random

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI
from sqlmodel import Session

from sdxl import SDAPIAsync
from db import new_engine
from db.models import GeneratedFiles
from db.helpers import process_request

phrases = [
    "I'm so excited to share this with you! I poured my heart into every brushstroke, and I hope it brings as much joy to you as it did to me while creating it.",
    "Here it is, the artwork you envisioned! I've infused it with vibrant colors and delicate details, hoping it captures the essence of what you imagined.",
    "Ta-da! Your vision has come to life on this canvas. I've added a touch of whimsy and lots of love, just for you.",
    "I've been eagerly waiting to reveal this to you! It's a blend of your ideas and my artistic touch, creating something truly unique.",
    "Look what I've created for you! It's not just a painting; it's a piece of my soul, intertwined with your wonderful idea.",
    "I'm thrilled to unveil this piece to you! Every detail is crafted with care, reflecting both your vision and my artistic journey.",
    "This is the moment! Your dream has been transformed into art, with a sprinkle of my creative magic.",
    "Voilà! Your idea has blossomed into a beautiful reality on this canvas, crafted with love and a dash of playfulness.",
    "I can't wait for you to see this! It's a fusion of your thoughts and my artistic flair, all wrapped up in vibrant colors and textures.",
    "Here's the masterpiece you inspired! I've woven in your concepts with my artistic interpretation for something truly special.",
    "I'm so happy to present this to you! Every stroke and hue has been chosen to resonate with your vision and my artistic voice.",
    "Your idea has been brought to life! It's not just a painting, it's a conversation between your imagination and my creativity.",
    "Prepare to be delighted! This artwork is a blend of your wonderful concept and my passion for creating something beautiful.",
    "Here it is, the artwork we dreamed up together! It's filled with joy, color, and a little piece of my heart.",
    "I've been bubbling with excitement to show you this! It's a dance of your ideas and my brushstrokes, creating a visual harmony just for you."
]


class ImageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        self.sdxl = SDAPIAsync(base_url=os.getenv("SD_API_URL"))
        log.info("Loaded ImageCog")

    @nextcord.slash_command(name="imagine", description="Have Sam draw for you!")
    async def _imagine(self, interaction: nextcord.Interaction, prompt: str,
                       quality: str | None = nextcord.SlashOption(name="quality", description="Image quality", required=False, choices=['normal', 'best', 'best - uncensored'], default='normal')):
        _, request, _ = process_request(
            self.engine, interaction, prompt, 'image', quality)
        log.info(
            f"Generating {quality} quality image with prompt: {prompt}")
        model = 'dall-e-2'
        if quality == 'best':
            model = 'dall-e-3'
        if 'uncensored' in quality:
            model = "sdxl"
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
            size = 0
            images = []
            image_data = resp.data
            # while it responds with a list of images, it only ever returns one
            for image in image_data:
                img = io.BytesIO(base64.b64decode(image.b64_json))
                img.seek(0)
                images.append(nextcord.File(
                    img, filename=f"{uuid.uuid4()}.jpg"))
                size += img.getbuffer().nbytes
            await interaction.followup.send(content=random.choice(phrases), files=images)
            log.info(
                f"Generated image with full prompt: {image.revised_prompt or prompt}")
        else:
            if not interaction.channel.is_nsfw() and 'uncensored' in quality:
                await interaction.followup.send("Cannot generate uncensored image in a non-NSFW channel.")
                return
            image = await self.sdxl.generate_image(prompt=prompt, width=1024, height=1024, negative_prompt=' watermark, disfigured, bad art, deformed, poorly drawn, extra limbs, close up, b&w, weird colors, blurry, depth of field, missing fingers, ugly face, extra legs')
            size = image.getbuffer().nbytes
            image.seek(0)
            await interaction.followup.send(content=random.choice(phrases), file=nextcord.File(image, filename=f"{uuid.uuid4()}.jpg"))
        with Session(self.engine) as session:
            f = GeneratedFiles(
                req_id=request.id,
                file_type='image',
                size=size,
            )
            session.add(f)
            session.commit()

    @_imagine.error
    async def _imagine_error(self, ctx: nextcord.Interaction, error: commands.CommandError):
        log.error(f"Error generating image: {error}")
        error_message = str(error)
        if len(error_message) > 1800:
            error_message = error_message[:1800]
        try:
            await ctx.followup.send(f"Error generating image: {error_message}", ephemeral=True)
        except:
            await ctx.send(f"Error generating image: {error_message}", ephemeral=True)


def setup(bot):
    bot.add_cog(ImageCog(bot))
