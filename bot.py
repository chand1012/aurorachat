import os
import io
import base64
import uuid

import nextcord
from nextcord.ext import commands
from nextcord.iterators import HistoryIterator
from dotenv import load_dotenv
from openai import OpenAI
from loguru import logger as log

from ai import MAX_TOKENS, count_tokens, req, conversation_handler
from utils import truncate_string, split_messages
from sdxl import SDAPIAsync

load_dotenv()

o = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
sdxl = SDAPIAsync(base_url=os.getenv("SD_API_URL"))
# Load environment variables from .env file

# Get the bot token from the environment variable
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TESTING_GUILD_ID = int(os.getenv('TESTING_GUILD_ID', '0')
                       )  # Replace with your guild ID
FORCE_GLOBAL = TESTING_GUILD_ID == 0
guild_ids = [TESTING_GUILD_ID]  # Put your server ID in this array.
# Define the intents (if required for your bot, otherwise you can omit this)
intents = nextcord.Intents.default()

# Define the bot instance with the command_prefix (it can be anything but is required to create the bot object)
bot = commands.Bot(intents=intents)

CHAT_MODELS = {
    'normal': 'gpt-3.5-turbo',
    'better': 'gpt-3.5-turbo-16k',
    'best': 'gpt-4'
}


@bot.event
async def on_ready():
    log.info(f"Logged in as {bot.user.name}#{bot.user.discriminator}")


@bot.event
async def on_message(message: nextcord.Message):
    if message.author == bot.user:
        return

    if message.channel.type == nextcord.ChannelType.public_thread or message.channel.type == nextcord.ChannelType.private_thread:
        # check if the bot is the one who started the thread
        if message.channel.owner != bot.user:
            return
        log.info(
            f'Received message in thread on {message.guild.name} ({message.guild.id})')
        async with message.channel.typing():
            # get the name and remove the "Chat-" part
            quality = message.channel.name.split(" - ")[2].strip()
            model = CHAT_MODELS[quality]
            log.info(f"Using model: {model}")
            # get the prompt from the user. Its the just sent message
            prompt = message.content
            tokens = count_tokens(prompt)
            # check if the prompt is too long
            if tokens > MAX_TOKENS[model]:
                await message.channel.send(f"Prompt is too long. Max tokens: {MAX_TOKENS[model]}")
                return
            try:
                messages = await conversation_handler(bot, message.channel.history(), prompt, model, tokens)
                response = req(o, messages)
                if len(response) > 2000:
                    # split until the message is less than 2000 characters
                    responses = split_messages(response)
                    for response in responses:
                        await message.channel.send(response)
                else:
                    await message.channel.send(response)
            except Exception as e:
                log.error(f"Error generating response: {e}")
                await message.channel.send("There was an error generating a response. Please try again later.")


@bot.slash_command(name="ping", description="Get the bot's current latency", guild_ids=guild_ids, force_global=FORCE_GLOBAL)
async def ping(interaction: nextcord.Interaction):
    latency = round(bot.latency * 1000)  # convert from seconds to ms
    await interaction.response.send_message(f"Pong! {latency}ms")


@bot.slash_command(name="imagine", description="Have Sam draw for you!", guild_ids=guild_ids, force_global=FORCE_GLOBAL)
async def _imagine(interaction: nextcord.Interaction,
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
        resp = o.images.generate(
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
            images.append(nextcord.File(img, filename=f"{uuid.uuid4()}.jpg"))
        await interaction.followup.send(content=f"Full prompt: `{image.revised_prompt or prompt}`", files=images)
        log.info(
            f"Generated image with full prompt: {image.revised_prompt or prompt}")
    else:
        if not interaction.channel.is_nsfw() and uncensored == 'true':
            await interaction.followup.send("Cannot generate uncensored image in a non-NSFW channel.")
            return
        image = await sdxl.generate_image(prompt=prompt, width=1024, height=1024, negative_prompt=' watermark, disfigured, bad art, deformed, poorly drawn, extra limbs, close up, b&w, weird colors, blurry, depth of field, missing fingers, ugly face, extra legs')
        await interaction.followup.send(content=f"Full prompt: `{prompt}`", file=nextcord.File(image, filename=f"{uuid.uuid4()}.jpg"))


@_imagine.error
async def _imagine_error(ctx: nextcord.Interaction, error: commands.CommandError):
    log.error(f"Error generating image: {error}")
    try:
        await ctx.followup.send(f"Error generating image: {error}", ephemeral=True)
    except:
        await ctx.send(f"Error generating image: {error}", ephemeral=True)


@bot.slash_command(
    name="chat",
    description="Chat with Sam",
)
async def _chat(ctx: nextcord.Interaction, quality: str | None = nextcord.SlashOption(name="quality", description="Quality of conversation", required=False, choices=['normal', 'better', 'best'], default='normal'), prompt: str | None = nextcord.SlashOption(name="prompt", description="The initial message to send", required=False)):
    model = CHAT_MODELS[quality]
    await ctx.response.defer(ephemeral=False)
    log.info(
        f"Creating new thread with quality '{quality}' ({model}) for on {ctx.guild.name} ({ctx.guild.id}. Initial message: '{prompt}')")
    # needs to make the initial request to chatgpt
    thread_name = f"Thread - {truncate_string(prompt) if prompt else 'New Chat'} - {quality}"
    thread = await ctx.channel.create_thread(name=thread_name, type=nextcord.ChannelType.public_thread)
    await ctx.followup.send(f"Created thread {thread.mention}")
    if prompt is None:
        await thread.send("Hello! I am Sam, your helpful assistant. How can I help you today?")
    else:
        async with thread.typing():
            messages = [
                {'role': 'assistant',
                    'content': 'Hello! I am Sam, your helpful assistant. How can I help you today?'},
                {'role': 'user', 'content': prompt}
            ]

            response = req(o, messages)
            if len(response) > 2000:
                # split until the message is less than 2000 characters
                responses = split_messages(response)
                for response in responses:
                    await thread.send(response)
            else:
                await thread.send(response)


@_chat.error
async def _chat_error(ctx: nextcord.Interaction, error: commands.CommandError):
    log.error(f"Error starting chat: {error}")
    try:
        await ctx.followup.send(f"Error starting chat: {error}", ephemeral=True)
    except:
        await ctx.send(f"Error starting chat: {error}", ephemeral=True)


@bot.slash_command(
    name="delete",
    description="Delete the thread. Does nothing if the bot is not the owner or if not in a thread.",
)
async def _delete(ctx: nextcord.Interaction):
    if ctx.channel.type == nextcord.ChannelType.public_thread or ctx.channel.type == nextcord.ChannelType.private_thread:
        if ctx.channel.owner != bot.user:
            return
        await ctx.channel.delete()


@_delete.error
async def _delete_error(ctx: nextcord.Interaction, error: commands.CommandError):
    log.error(f"Error deleting thread: {error}")
    try:
        await ctx.followup.send(f"Error deleting thread: {error}", ephemeral=True)
    except:
        await ctx.send(f"Error deleting thread: {error}", ephemeral=True)


@bot.slash_command(
    name="speak",
    description="Have Sam speak for you!",
    guild_ids=guild_ids,
    force_global=FORCE_GLOBAL
)
async def _speak(ctx: nextcord.Interaction, prompt: str):
    log.info(f"Generating speech with prompt: {prompt}")
    await ctx.response.defer(ephemeral=False)
    resp = o.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=prompt,
        response_format="mp3",
        speed=0.9
    )
    byte_stream = io.BytesIO(resp.content)
    byte_stream.seek(0)
    await ctx.followup.send(file=nextcord.File(byte_stream, filename=f"{uuid.uuid4()}.mp3"))


@_speak.error
async def _speak_error(ctx: nextcord.Interaction, error: commands.CommandError):
    log.error(f"Error generating speech: {error}")
    try:
        await ctx.followup.send(f"Error generating speech: {error}", ephemeral=True)
    except:
        await ctx.send(f"Error generating speech: {error}", ephemeral=True)


@bot.slash_command(
    name="upload",
    description="Upload a file to the bot",
)
async def _upload(ctx: nextcord.Interaction, attachment: nextcord.Attachment):
    # for now just save the attachment to a file
    await ctx.response.defer(ephemeral=False)
    await attachment.save(f"{attachment.filename}")
    await ctx.followup.send(f"Saved {attachment.filename} to uploads folder")

# Make sure this is the main file being run, not a module being imported
if __name__ == "__main__":
    bot.run(BOT_TOKEN)
