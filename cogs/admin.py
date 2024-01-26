# retrieval and generation cog
import os

from nextcord.ext import commands
import nextcord
from loguru import logger as log
from sqlmodel import Session, select
from openai import OpenAI

from athenadb import AthenaDB
from db import new_engine
from db.models import Overrides
# from db.helpers import process_request, process_text_response
from utils.webhooks import send_error_webhook
from utils.strings import split_text_into_chunks
from utils.upload import process_docx, process_pdf


class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.engine = new_engine()
        self.openai = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.athena = AthenaDB(os.getenv('ATHENA_DB'))
        log.info("Loaded AdminCog")

    @nextcord.slash_command(name="set_quickchat_prompt", description="Set the system prompt for quickchat.")
    async def set_quickchat_prompt(self, interaction: nextcord.Interaction, prompt: str = nextcord.SlashOption(name="prompt", description="Prompt for the quickchat system", required=True)):
        await interaction.response.defer()
        # check if the user is a mod
        if not interaction.user.guild_permissions.administrator:
            await interaction.followup.send("Sorry, you must be a server administrator to use this command.")
            return
        # prompt must be less than a discord message (2k chars)
        if len(prompt) > 2000:
            await interaction.followup.send("Sorry, that prompt is too long. Please keep it under 2000 characters.")
            return
        self.engine = new_engine()
        with Session(self.engine) as session:
            # if there's already a prompt, update it
            statement = select(Overrides).where(
                Overrides.guild_id == str(interaction.guild.id))
            result = session.exec(statement).first()
            if result:
                result.quickchat_system_prompt = prompt
                session.commit()
                await interaction.followup.send(f'Successfully updated the quickchat prompt to "{prompt}".')
                return
            # otherwise, add it
            session.add(Overrides(
                guild_id=str(interaction.guild.id), quickchat_system_prompt=prompt))
            session.commit()
            await interaction.followup.send(f'Successfully set the quickchat prompt to "{prompt}".')

    @set_quickchat_prompt.error
    async def set_quickchat_prompt_error(self, interaction: nextcord.Interaction, error: commands.CommandError):
        await interaction.followup.send('Sorry! There was an error setting the quickchat prompt. If this issue persists please contact support. See `/support` for more information.')
        send_error_webhook('Error setting quickchat prompt!', 'set_quickchat_prompt', str(interaction.channel_id), str(
            interaction.message.id), str(interaction.user.id), f'Error: {error}')

    @nextcord.slash_command(name="get_quickchat_prompt", description="Get the system prompt for quickchat.")
    async def get_quickchat_prompt(self, interaction: nextcord.Interaction):
        await interaction.response.defer()
        # check if the user is a mod
        if not interaction.user.guild_permissions.administrator:
            await interaction.followup.send("Sorry, you must be a server administrator to use this command.")
            return
        self.engine = new_engine()
        with Session(self.engine) as session:
            # if there's already a prompt, update it
            statement = select(Overrides).where(
                Overrides.guild_id == str(interaction.guild.id))
            result = session.exec(statement).first()
            if result:
                if result.quickchat_system_prompt:
                    await interaction.followup.send(f'The current quickchat prompt is "{result.quickchat_system_prompt}".')
                    return
            await interaction.followup.send('There is no current quickchat prompt.')

    @get_quickchat_prompt.error
    async def get_quickchat_prompt_error(self, interaction: nextcord.Interaction, error: commands.CommandError):
        await interaction.followup.send('Sorry! There was an error getting the quickchat prompt. If this issue persists please contact support. See `/support` for more information.')
        send_error_webhook('Error getting quickchat prompt!', 'get_quickchat_prompt', str(interaction.channel_id), str(
            interaction.message.id), str(interaction.user.id), f'Error: {error}')

    #  Currently only supports plain text documents (.txt), Markdown (.md), PDFs (.pdf), HTML Web Pages (.html), and Word (.docx) documents. Plain text, HTML Web Pages, and Markdown must be UTF-8 encoded.
    @nextcord.slash_command(name="add_docs_quickchat", description="Give Aurora some information to search for when using quickchat.")
    async def add_docs_quickchat(self, interaction: nextcord.Interaction, doc: nextcord.Attachment):
        await interaction.response.defer()
        # check if the user is a mod
        if not interaction.user.guild_permissions.administrator:
            await interaction.followup.send("Sorry, you must be a server administrator to use this command.")
            return
        # check by extension
        ext = doc.filename.split('.')[-1]
        if not doc.filename.endswith(('.txt', '.md', '.pdf', '.docx')):
            send_error_webhook('Invalid file type!', 'add_docs_quickchat', str(interaction.channel_id), str(
                interaction.message.id), str(interaction.user.id), f'File type: {ext}')
            await interaction.followup.send("Sorry, that file type is not supported. Currently only plain text documents (.txt), Markdown (.md), PDFs (.pdf), and Word (.docx) documents are supported.")
            return
        # has to be under 8MB
        if doc.size > 8000000:
            await interaction.followup.send("Sorry, that file is too large. Please keep it under 8MB.")
            return

        content = ''
        raw_content = await doc.read()
        match ext:
            case 'txt' | 'md':
                content = raw_content.decode('utf-8')
            case 'pdf':
                content = process_pdf(raw_content)
            case 'docx':
                content = process_docx(raw_content)
            case _:
                await interaction.followup.send("Sorry, that file type is not supported. Currently only plain text documents (.txt), Markdown (.md), PDFs (.pdf), and Word (.docx) documents are supported.")
                return

        if len(content) < 100:
            await interaction.followup.send("There seems to be an issue with your file, its rather short. Please make sure it is a valid file and try again.")
            send_error_webhook('File too short!', 'add_docs_quickchat', str(interaction.channel_id), str(
                interaction.message.id), str(interaction.user.id), f'File content: {doc.url}')
            return

        chunks = split_text_into_chunks(content)
        # I'm going to attempt to do this in a single transaction
        # if not we'll have to further chunk the chunks
        namespace = f'server.{interaction.guild.id}.quickchat'
        await self.athena.insert(inputs=chunks, namespace=namespace)
        await interaction.followup.send(f"Successfully added {doc.filename} to the quickchat database.")
        self.engine = new_engine()
        with Session(self.engine) as session:
            # check if an override with this namespace already exists
            statement = select(Overrides).where(
                Overrides.guild_id == str(interaction.guild.id))
            result = session.exec(statement).first()
            if result:
                if result.athena_namespace == namespace:
                    return
                else:
                    result.athena_namespace = namespace
                    session.commit()
                    return
            session.add(Overrides(
                guild_id=str(interaction.guild.id), athena_namespace=namespace))
            session.commit()

    @add_docs_quickchat.error
    async def add_docs_quickchat_error(self, interaction: nextcord.Interaction, error: commands.CommandError):
        await interaction.followup.send('Sorry! There was an error adding the document to the quickchat database. If this issue persists please contact support. See `/support` for more information.')
        send_error_webhook('Error adding document to quickchat database!', 'add_docs_quickchat', str(interaction.channel_id), str(
            interaction.message.id), str(interaction.user.id), f'Error: {error}')


def setup(bot: commands.Bot):
    bot.add_cog(AdminCog(bot))
