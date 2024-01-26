import os
import asyncio
import io
import uuid
import random

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from httpx import AsyncClient
from sqlmodel import Session
import humanize

from db import new_engine
from db.models import GeneratedFiles
from db.helpers import process_request
from utils.webhooks import send_error_webhook

phrases = [
    "Excited to share this meme with you! I had a blast creating it and hope it brings a smile to your face.",
    "Here's the meme you requested. I've blended humor with a clever twist, hoping it's just what you were looking for.",
    "Ta-da! I've transformed your idea into a meme, adding a sprinkle of fun to it.",
    "Proud to present this meme to you. It's a fusion of your concept and my sense of humor, creating something unique.",
    "Check out this meme I crafted for you. It's not just a joke; it's a blend of your brilliant idea and my quirky creativity.",
    "Super excited for you to see this meme. I've fine-tuned every detail to capture both your vision and my comedic style.",
    "Here it is! I've turned your vision into a hilarious meme, infused with a dash of my own creativity.",
    "Ready for a laugh? Your idea has now been transformed into a delightful meme, created with care and humor.",
    "Can't wait for you to see this. It's a meld of your fun thoughts and my meme-making skills, with a twist of wit.",
    "Presenting the meme inspired by you. I've merged your suggestions with my humor to create something truly entertaining.",
    "Glad to show you this meme. I chose each element carefully to align with your idea and my flair for comedy.",
    "Your concept is now a meme! It's more than a joke; it's a mix of your imagination and my sense of humor.",
    "Get ready to chuckle! This meme blends your fantastic idea with my passion for comedy.",
    "Here's the meme we brainstormed. It's packed with laughs, creativity, and a personal touch from me.",
    "I've been eager to show you this. It's a mix of your funny ideas and my meme-making, aiming to tickle your funny bone."
]


class MemeGenCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = os.getenv('COMPANYHERD_URL')
        self.client = AsyncClient(base_url=self.url, verify=False)
        self.engine = new_engine()
        log.info("Loaded MemeGenCog")

    @nextcord.slash_command(name="meme", description="Have Aurora make a meme for you!")
    async def _meme(self, interaction: nextcord.Interaction, prompt: str = nextcord.SlashOption(name="prompt", description="Prompt for the meme", required=True)):
        await interaction.response.defer()
        self.engine = new_engine()
        _, request, time_remaining = process_request(
            self.engine, interaction, prompt, 'meme', 'meme')
        if time_remaining is not None:
            await interaction.followup.send(f"Sorry, you've reached the free limit for today. Please try again in {humanize.precisedelta(time_remaining)}", ephemeral=True)
            return
        log.info(
            f"User {interaction.user.id} requested a meme with prompt {prompt}")
        # make a request to /meme with the prompt in the query string as "topic"
        resp = await self.client.get("/meme", params={"topic": prompt})
        if resp.status_code != 200:
            log.error(
                f"Got status code {resp.status_code} from meme endpoint")
            resp.raise_for_status()
        task_id = resp.json()['task_id']
        image_url = None
        while image_url is None:
            await asyncio.sleep(2)
            resp = await self.client.get(f"/task/{task_id}")
            if resp.status_code != 200:
                log.error(
                    f"Got status code {resp.status_code} from meme endpoint")
                resp.raise_for_status()

            data = resp.json()
            if data['status'] == 'SUCCESS':
                image_url = data['result']
            elif data['status'] == 'FAILURE':
                raise Exception(
                    f'Failed to generate meme: CompanyHerd task {task_id} failed')
        # download the image
        resp = await self.client.get(image_url)
        if resp.status_code != 200:
            log.error(
                f"Got status code {resp.status_code} from meme endpoint")
            resp.raise_for_status()

        # convert to bytesio
        image_bytes = io.BytesIO(resp.content)
        image_bytes.seek(0)
        # get the size
        size = image_bytes.getbuffer().nbytes
        image_bytes.seek(0)
        # upload to discord
        f = nextcord.File(image_bytes, filename=f"{uuid.uuid4()}.jpg")
        await interaction.followup.send(content=random.choice(phrases) + f' Prompt: {prompt}', file=f)
        with Session(self.engine) as session:
            g = GeneratedFiles(
                req_id=request.id,
                file_type="meme",
                size=size
            )
            session.add(g)
            session.commit()

    @_meme.error
    async def _meme_error(self, interaction: nextcord.Interaction, error: commands.CommandError):
        log.error(error)
        await send_error_webhook(str(error), 'meme_gen', interaction.channel_id, interaction.id, interaction.user.id, '')
        await interaction.followup.send("Sorry, something went wrong. Please try again later.")


def setup(bot):
    bot.add_cog(MemeGenCog(bot))
