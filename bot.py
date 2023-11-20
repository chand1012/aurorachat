import os

import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from loguru import logger as log

load_dotenv()

# Get the bot token from the environment variable
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = nextcord.Intents.default()
intents.message_content = True
# Define the bot instance with the command_prefix (it can be anything but is required to create the bot object)
bot = commands.Bot(intents=intents)


@bot.event
async def on_ready():
    log.info(f"Logged in as {bot.user.name}#{bot.user.discriminator}")

# Make sure this is the main file being run, not a module being imported
if __name__ == "__main__":
    bot.load_extension('cogs.ping')
    bot.load_extension('cogs.chat')
    bot.load_extension('cogs.images')
    bot.load_extension('cogs.tts')
    bot.load_extension('cogs.summary')
    bot.load_extension('cogs.cleaner')
    bot.run(BOT_TOKEN)
