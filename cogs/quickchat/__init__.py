import os

from nextcord.ext import commands
import nextcord
from loguru import logger as log
# from sqlmodel import Session


from ai import WorkersAILLMClient
from db import new_engine
# from db.helpers import process_request


class QuickChatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.engine = new_engine()
        self.ai = WorkersAILLMClient()
        log.info("Loaded QuickChatCog")

    # listen for messages
    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author == self.bot.user:
            return
        # the message has to mention the bot
        if not message.mentions or message.mentions[0] != self.bot.user:
            return

        # the message has to be in a regular channel. Not a DM, not a thread, not a group DM
        if not isinstance(message.channel, nextcord.TextChannel):
            return

        async with message.channel.typing():
            log.info(
                f'QuickChat from {message.author} on {message.channel.id}: {message.content}')
            prompt = message.content
            # remove the mention from the prompt
            prompt = prompt.replace(f'<@{self.bot.user.id}>', 'Aurora,')
            prompt = prompt.strip()
            # _, _, allowed = process_request(
            #     self.engine, message, prompt, 'text', 'free')
            messages = self.ai.format_prompt(prompt)
            response = await self.ai.run(messages)
            response = response.strip()
            log.info(
                f'QuickChat from {message.author} on {message.channel.id}: {response}')
            # for now just echo the prompt back and print to the console
            await message.channel.send(response, reference=message)


def setup(bot: commands.Bot):
    bot.add_cog(QuickChatCog(bot))
