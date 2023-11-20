# from datetime import datetime, timedelta

import nextcord
from sqlmodel import Session, select
from sqlalchemy.engine.base import Engine

from db.models import Request, User


def process_request(engine: Engine, interaction: nextcord.Interaction | nextcord.Message, prompt: str, req_type: str, quality: str):
    '''Takes in a request and processes it, returning true if the user can continue to the next step, false otherwise'''
    discord_user_id = None
    message_id = None
    if isinstance(interaction, nextcord.Interaction):
        discord_user_id = str(interaction.user.id)
        message_id = str(interaction.message.id)
    elif isinstance(interaction, nextcord.Message):
        discord_user_id = str(interaction.author.id)
        message_id = str(interaction.id)
    else:
        raise TypeError(
            f"Expected interaction or message, got {type(interaction)}")
    with Session(engine) as session:
        # first check if a user exists with the given discord id
        statement = select(User).where(
            User.discord_id == discord_user_id)
        user = session.exec(statement).first()
        if user is None:
            # create a new user
            user = User(discord_id=discord_user_id)
            session.add(user)
            session.commit()
            user = session.exec(statement).first()

        req = Request(
            user_id=user.id,
            prompt=prompt,
            req_type=req_type,
            quality=quality,
            guild_id=str(interaction.guild.id),
            channel_id=str(interaction.channel.id),
            message_id=message_id
        )
        session.add(req)
        session.commit()
        # get the request's id
        req = session.exec(select(Request).where(
            Request.user_id == user.id).where(Request.prompt == prompt)).first()

        # # get the number of requests the user has made in the last 720 hours
        # statement = select(Request).where(
        #     Request.user_id == user.id).where(Request.created_at > datetime.now() - timedelta(hours=720))

        # num_requests = len(session.exec(statement).all())

        # TODO this is where we'll ratelimit based on use
        # if num_requests >= 5:
        #     # user has made too many requests
        #     return user, None, False

        return user, req, True
