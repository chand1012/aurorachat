import os
import nextcord
from nextcord.ext import commands
from loguru import logger as log

from cogs.help.constants import long_descriptions, support_server_link
from utils import random_color_in_gradient, hex_to_int


class HelpCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        log.info("Loaded HelpCog")

    @nextcord.slash_command(name="help", description="Show this help text.")
    async def _help(self, interaction: nextcord.Interaction, command: str | None = nextcord.SlashOption(name="command", description="Command to get help for", required=False)):
        """Help command for slash commands"""
        color = hex_to_int(random_color_in_gradient('#211171', '#00FDC3'))

        if not command:
            embed = nextcord.Embed(title="Help - Slash Commands",
                                   description="Hello! I'm Aurora, your Discord AI Assistant. Here is a list of all the commands that I can do. Type `/help <command>` for more information.", color=color)

            for cmd in self.bot.get_application_commands():
                # Add command name and description to the embed
                embed.add_field(
                    name=f"/{cmd.name}", value=cmd.description or "No description", inline=False)

            await interaction.response.send_message(embed=embed)
        else:
            long_desc = long_descriptions.get(command)
            if not long_desc:
                await interaction.response.send_message("Command not found.")
                return
            embed = nextcord.Embed(
                title=f"Help - /{command}", description=long_desc, color=color)
            await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="support", description="Display support contact information.")
    async def support(self, interaction: nextcord.Interaction):
        """Support command for slash commands"""
        color = hex_to_int(random_color_in_gradient('#211171', '#00FDC3'))

        embed = nextcord.Embed(title="Support - Aurora",
                               description="Need help? Contact us!", color=color)
        embed.add_field(name="Support Server",
                        value=f"[Click here]({support_server_link})")
        # embed.add_field(name="Email", value="aurora@timesurgelabs.com")
        embed.add_field(
            name="Website", value="https://aurora.timesurgelabs.com")
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(HelpCog(bot))
