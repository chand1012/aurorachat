import os
import nextcord
from nextcord.ext import commands
from loguru import logger as log

from cogs.help.constants import HELP_MESSAGE


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        log.info("Loaded HelpCog")

    @nextcord.slash_command(name="help", description="Get help with using the bot")
    async def _help(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(HELP_MESSAGE)


def setup(bot):
    bot.add_cog(HelpCog(bot))
