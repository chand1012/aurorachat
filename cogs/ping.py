import nextcord
from nextcord.ext import commands
from loguru import logger as log
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond with a 200 status code and 'ok' text
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
        self.server_thread = threading.Thread(target=self.httpd.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
        log.info("Loaded PingCog")

    def cog_unload(self):
        # Shutdown the HTTP server when the cog is removed
        self.httpd.shutdown()
        self.server_thread.join()

    @nextcord.slash_command(name="ping", description="Get the bot's current latency")
    async def ping(self, interaction: nextcord.Interaction):
        latency = round(self.bot.latency * 1000)  # convert from seconds to ms
        await interaction.response.send_message(f"Pong! {latency}ms")

    @ping.error
    async def ping_error(self, interaction: nextcord.Interaction, error: commands.CommandError):
        await interaction.response.send_message(f"Error: {error}")


def setup(bot):
    bot.add_cog(PingCog(bot))
