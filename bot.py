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
bot = commands.Bot(intents=intents, help_command=None)


@bot.event
async def on_ready():
    log.info(f"Logged in as {bot.user}")

# Make sure this is the main file being run, not a module being imported
if __name__ == "__main__":
    log.info("Loading cogs, this may take up to a minute...")
    bot.load_extension('cogs.help')
    bot.load_extension('cogs.ping')
    bot.load_extension('cogs.admin')
    bot.load_extension('cogs.chat')
    bot.load_extension('cogs.quickchat')
    bot.load_extension('cogs.memegen')
    bot.load_extension('cogs.images')
    bot.load_extension('cogs.tts')
    bot.load_extension('cogs.summary')
    bot.load_extension('cogs.cleaner')
    bot.load_extension('cogs.feedback')
    bot.run(BOT_TOKEN)
