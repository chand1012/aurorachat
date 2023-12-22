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
import humanize

from sdxl import WorkersSDAPIAsync, SDAPIAsync
from db import new_engine
from db.models import GeneratedFiles
from db.helpers import process_request
from utils.webhooks import send_error_webhook

phrases = [
    "I'm happy to share this with you. I put a lot of effort into it and hope you like it as much as I enjoyed making it.",
    "Here's the artwork you asked for. I've used bright colors and fine details, and I hope it's close to what you had in mind.",
    "Here it is! I brought your idea to the canvas and added a little fun twist to it.",
    "I'm glad to finally show this to you. It's a mix of your ideas and my style, making something different.",
    "Take a look at what I've made for you. It's more than a painting; it's a bit of me and your great idea combined.",
    "I'm excited to show you this piece. I've paid attention to every detail, hoping to reflect both your vision and my own style.",
    "This is it! I've turned your dream into art with a bit of my own creativity.",
    "Here we go! Your idea is now a lovely painting, made with care and a bit of fun.",
    "I'm eager for you to see this. It's a combination of your thoughts and my artistic style, with lots of colors and textures.",
    "Here's the artwork you inspired. I've blended your ideas with my interpretation to create something special.",
    "I'm glad to present this to you. I chose each stroke and color to match your vision and my artistic approach.",
    "Your idea is now a reality. It's more than just a painting; it's a blend of your imagination and my creative touch.",
    "Get ready to enjoy this! This artwork mixes your great concept with my love for creating beauty.",
    "Here's the artwork we came up with together. It's full of joy, color, and a bit of my personal touch.",
    "I've been looking forward to showing you this. It's a combination of your ideas and my painting, aiming for a visual harmony just for you."
]

NEGATIVE_PROMPT = "watermark, disfigured, bad art, deformed, poorly drawn, extra limbs, close up, b&w, weird colors, blurry, depth of field, missing fingers, ugly face, extra legs"


class ImageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        self.sdxl_modal = SDAPIAsync(base_url=os.getenv("SD_API_URL"))
        self.sdxl = WorkersSDAPIAsync()
        log.info("Loaded ImageCog")

    @nextcord.slash_command(name="imagine", description="Have Aurora draw for you!")
    async def _imagine(self, interaction: nextcord.Interaction, prompt: str = nextcord.SlashOption(name="prompt", description="Prompt for the image", required=True),
                       quality: str | None = nextcord.SlashOption(name="quality", description="Image quality", required=False, choices=[
                                                                  'normal', 'better', 'best', 'uncensored'], default='normal'),
                       negative_prompt: str = nextcord.SlashOption(name="negative_prompt", description="Negative prompt for the image. Only supported on \"best\" and \"uncensored\" qualities.", required=False, default=NEGATIVE_PROMPT)):
        _, request, time_remaining = process_request(
            self.engine, interaction, prompt, 'image', quality)
        if time_remaining is not None:
            await interaction.response.send_message(f"Sorry, you've reached the free limit for today. Please try again in {humanize.precisedelta(time_remaining)}", ephemeral=True)
            return
        log.info(
            f"Generating {quality} quality image with prompt: {prompt}")
        model = 'dall-e-3'
        if not 'better' in quality:
            model = 'sdxl'
        await interaction.response.defer()
        if 'dall-e' in model:
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
            sdxl = self.sdxl
            if not 'uncensored' in quality:
                resp = self.openai.moderations.create(
                    model="text-moderation-stable",
                    input=prompt,
                )
                if len(resp.results) == 0:
                    raise Exception(
                        'content_policy_violation: failed moderation')
                if resp.results[0].flagged:
                    raise Exception(
                        'content_policy_violation: failed moderation')

            if 'best' or 'uncensored' in quality:
                sdxl = self.sdxl_modal
            image = await sdxl.generate_image(prompt=prompt, negative_prompt=negative_prompt)
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
        if 'content_policy_violation' in error_message:
            error_message = "Content policy violation for model. Please try again with a different prompt or try a different model."
        if 'unavailable' in error_message:
            error_message = "Model is currently under high loads. Please try a different model or try again later."
        if len(error_message) > 1800:
            error_message = error_message[:1800]
        try:
            await ctx.followup.send(f"Error generating image: {error_message}", ephemeral=True)
        except:
            await ctx.send(f"Error generating image: {error_message}", ephemeral=True)
        if 'content_policy_violation' in error_message:
            return
        await send_error_webhook(error_message, 'imagine', ctx.channel.id, ctx.message.id,
                                 ctx.author.id, ctx.message.content)


def setup(bot):
    bot.add_cog(ImageCog(bot))
