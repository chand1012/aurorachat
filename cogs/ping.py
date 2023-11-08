import nextcord
from nextcord.ext import commands
from loguru import logger as log


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        log.info("Loaded PingCog")

    @nextcord.slash_command(name="ping", description="Get the bot's current latency")
    async def ping(self, interaction: nextcord.Interaction):
        latency = round(self.bot.latency * 1000)  # convert from seconds to ms
        await interaction.response.send_message(f"Pong! {latency}ms")

    @ping.error
    async def ping_error(self, interaction: nextcord.Interaction, error: commands.CommandError):
        await interaction.response.send_message(f"Error: {error}")


def setup(bot):
    bot.add_cog(PingCog(bot))
