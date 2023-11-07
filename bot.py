import os
import io
import base64
import uuid
import asyncio

import nextcord
import tiktoken
from nextcord.ext import commands
from dotenv import load_dotenv
from openai import OpenAI
from loguru import logger as log

o = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load environment variables from .env file
load_dotenv()

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

enc = tiktoken.get_encoding("cl100k_base")

MAX_TOKENS = {
    "gpt-4": 8192,
    "gpt-3.5-turbo": 4096,
}

allowed_models = MAX_TOKENS.keys()


def count_tokens(text: str):
    return len(enc.encode(text))


def req(messages: list[dict]) -> str | list[str]:
    resp = o.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages)
    if len(resp.choices) == 0:
        return "No response"
    return resp.choices[0].message.content


def split_messages(content, max_len=2000):
    split = content.split("\n")
    responses = []
    current = ""
    for line in split:
        if len(current) + len(line) > max_len:
            responses.append(current)
            current = ""
        current += line + "\n"
        responses.append(current)
    return responses


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
        await message.channel.trigger_typing()
        # get the name and remove the "Chat-" part
        model = message.channel.name[5:]
        # check if the model is allowed
        if model not in allowed_models:
            model = "gpt-3.5-turbo"
        # get the prompt from the user. Its the just sent message
        prompt = message.content
        tokens = count_tokens(prompt)
        # check if the prompt is too long
        if tokens > MAX_TOKENS[model]:
            await message.channel.send(f"Prompt is too long. Max tokens: {MAX_TOKENS[model]}")
            return
        thread_messages = [{
            'role': 'system',
            'content': 'You are a helpful assistant.'
        }]
        # get previous messages in the thread
        # if it was a user, add { 'role': 'user', 'content': message.content }
        # if it was the bot, add { 'role': 'assistant', 'content': message.content }
        # count the tokens first and check if it is too long
        async for msg in message.channel.history():
            if msg.author == bot.user:
                thread_messages.append(
                    {'role': 'assistant', 'content': msg.content})
            else:
                thread_messages.append(
                    {'role': 'user', 'content': msg.content})
        thread_messages.reverse()
        messages = [{"role": "user", "content": prompt}]
        for msg in thread_messages:
            msg_tokens = count_tokens(msg['content'])
            if msg_tokens + tokens > MAX_TOKENS[model]:
                break
            messages.append(msg)
            tokens += msg_tokens
        messages.reverse()
        response = req(messages)
        if len(response) > 2000:
            # split until the message is less than 2000 characters
            responses = split_messages(response)
            for response in responses:
                await message.channel.send(response)
        else:
            await message.channel.send(response)


@bot.slash_command(name="ping", description="Get the bot's current latency", guild_ids=guild_ids, force_global=FORCE_GLOBAL)
async def ping(interaction: nextcord.Interaction):
    latency = round(bot.latency * 1000)  # convert from seconds to ms
    await interaction.response.send_message(f"Pong! {latency}ms")


@bot.slash_command(name="imagine", description="Generates an image via Dalle-3", guild_ids=guild_ids, force_global=FORCE_GLOBAL)
async def generate_image(interaction: nextcord.Interaction, prompt: str):
    log.info(f"Generating image with prompt: {prompt}")
    await interaction.response.defer()
    resp = o.images.generate(
        model="dall-e-3",
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
    await interaction.followup.send(content=f"Full prompt: `{image.revised_prompt}`", files=images)
    log.info(f"Generated image with full prompt: {image.revised_prompt}")


@bot.slash_command(
    name="chat",
    description="Chat with the AI model",
)
async def _chat(ctx: nextcord.Interaction, model: str | None = nextcord.SlashOption(name="model", description="The model to use", required=False, choices=allowed_models), initial_message: str | None = nextcord.SlashOption(name="initial_message", description="The initial message to send", required=False)):
    if model is None or model not in allowed_models:
        model = "gpt-3.5-turbo"
    await ctx.response.defer(ephemeral=False)
    log.info(
        f"Creating new thread for on {ctx.guild.name} ({ctx.guild.id}. Initial message: '{initial_message}')")
    # needs to make the initial request to chatgpt
    thread_name = f"Thread - {initial_message or model}"
    thread = await ctx.channel.create_thread(name=thread_name, type=nextcord.ChannelType.public_thread)
    await asyncio.sleep(1)
    if initial_message is None:
        await thread.send("Hello! I am Sam, your helpful assistant. How can I help you today?")
    else:
        await thread.trigger_typing()
        messages = [
            {'role': 'assistant',
                'content': 'Hello! I am Sam, your helpful assistant. How can I help you today?'},
            {'role': 'user', 'content': initial_message}
        ]

        response = req(messages)
        if len(response) > 2000:
            # split until the message is less than 2000 characters
            responses = split_messages(response)
            for response in responses:
                await thread.send(response)
        else:
            await thread.send(response)
        await ctx.response.send_message(f"Created thread {thread.mention}")


@bot.slash_command(
    name="delete",
    description="Delete the thread. Does nothing if the bot is not the owner or if not in a thread.",
)
async def _delete(ctx: nextcord.Interaction):
    if ctx.channel.type == nextcord.ChannelType.public_thread or ctx.channel.type == nextcord.ChannelType.private_thread:
        if ctx.channel.owner != bot.user:
            return
        await ctx.channel.delete()


# Make sure this is the main file being run, not a module being imported
if __name__ == "__main__":
    bot.run(BOT_TOKEN)
