import os

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from openai import OpenAI
from sqlmodel import Session
from loguru import logger as log

from db import new_engine

from cogs.feedback.process_feedback import process_feedback

rating_choices = {
    '👍':  1,
    '👎': -1,
    '😐':  0
}


class FeedbackCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.engine = new_engine()
        log.info("Loaded FeedbackCog")

    @nextcord.slash_command(name="goodbot", description="Tell Aurora she's a good bot!")
    async def _goodbot(self, interaction: nextcord.Interaction):
        # get the message history for the current channel. Get the last 20 messages, and get the last message that was sent by the bot
        last_message = None
        async for message in interaction.channel.history(limit=20):
            if message.author == self.bot.user:
                last_message = message
                break
        if last_message is None:
            await interaction.response.send_message("I don't think I've said anything yet.", ephemeral=True)
            return
        success = process_feedback(
            interaction, last_message, Session(self.engine), "goodbot", 1)
        if success is None:
            await interaction.response.send_message("I don't think I've said anything yet.", ephemeral=True)
            return
        if success is False:
            await interaction.response.send_message("You've already given feedback on this request.", ephemeral=True)
            return
        await interaction.response.send_message("Thank you! I try my best.", ephemeral=True)
        log.info(
            f'User {interaction.user} gave goodbot feedback on message {last_message.id} in channel {interaction.channel.id}')

    @nextcord.slash_command(name="badbot", description="Tell Aurora she's a bad bot!")
    async def _badbot(self, interaction: nextcord.Interaction):
        # get the message history for the current channel. Get the last 20 messages, and get the last message that was sent by the bot
        last_message = None
        async for message in interaction.channel.history(limit=20):
            if message.author == self.bot.user:
                last_message = message
                break
        if last_message is None:
            await interaction.response.send_message("I don't think I've said anything yet.", ephemeral=True)
            return
        success = process_feedback(
            interaction, last_message, Session(self.engine), "badbot", -1)
        if success is None:
            await interaction.response.send_message("I don't think I've said anything yet.", ephemeral=True)
            return
        if success is False:
            await interaction.response.send_message("You've already given feedback on this request.", ephemeral=True)
            return
        await interaction.response.send_message("I'm sorry! I'm just trying my best!", ephemeral=True)
        log.warning(
            f'User {interaction.user} gave badbot feedback on message {last_message.id} in channel {interaction.channel.id}')

    @nextcord.slash_command(name="feedback", description="Give feedback on a request!")
    async def _feedback(self, interaction: nextcord.Interaction,
                        feedback: str = nextcord.SlashOption(
                            name="feedback", description="The feedback to give Aurora.", required=True),
                        last_message: bool = nextcord.SlashOption(
                            name="last_message", description="Whether to give feedback on the last message sent by Aurora.", required=False, default=False),
                        rating: int = nextcord.SlashOption(choices=rating_choices, name="rating", description="The rating to give Aurora.", required=False, default=0)):
        # if the message is none do the same thing as goodbot/badbot
        message = None
        if last_message:
            # get the message history for the current channel. Get the last 20 messages, and get the last message that was sent by the bot
            # messages =
            last_message = None
            async for message in interaction.channel.history(limit=20):
                if message.author == self.bot.user:
                    last_message = message
                    break
            if last_message is None:
                await interaction.response.send_message("I don't think I've said anything yet.", ephemeral=True)
                return
            message = last_message
        success = process_feedback(
            interaction, message, Session(self.engine), feedback, rating)
        if success is None:
            await interaction.response.send_message("I don't think I've said anything yet.", ephemeral=True)
            return
        if success is False:
            await interaction.response.send_message("You've already given feedback on this request.", ephemeral=True)
            return
        await interaction.response.send_message("Thank you for your feedback!", ephemeral=True)
        if rating >= 0:
            log.info(
                f'User {interaction.user} gave feedback on message {message.id} in channel {interaction.channel.id}: {feedback}')
        else:
            log.warning(
                f'User {interaction.user} gave feedback on message {message.id} in channel {interaction.channel.id}: {feedback}')

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        # Check if the message is a reply
        if message.reference and message.reference.resolved:
            # Fetch the original message that is being replied to
            original_message = message.reference.resolved

            # Check if the bot is the author of the original message
            if original_message.author == self.bot.user:
                # if the original message is a reply do nothing
                if original_message.reference and original_message.reference.resolved:
                    return
                feedback = message.content
                success = process_feedback(
                    None, original_message, Session(self.engine), feedback)
                if success is None:
                    await message.channel.send("I don't think I've said anything yet.")
                    return
                if success is False:
                    await message.channel.send("You've already given feedback on this request.")
                    return
                await message.channel.send("Thank you for your feedback!")
                log.info(
                    f'User {message.author} gave feedback on message {original_message.id} in channel {message.channel.id}: {feedback}')


def setup(bot: commands.Bot):
    bot.add_cog(FeedbackCog(bot))
