from datetime import datetime, timedelta
from typing import List

import nextcord
from sqlmodel import Session, select
from sqlalchemy.engine.base import Engine
from loguru import logger as log

from db.models import Request, User, TextResponse, ServerOverrides

# both every 24 hours
FREE_LIMITS = {
    'text_free': 100,
    'text': 10,
    'image': 1,
    'image_normal': 3,
    'speak': 3,
    'meme': 3,
}

PAID_LIMITS = {
    'text_free': 500,
    'text': 400,
    'image': 10,
    'image_normal': 60,
    'speak': 100,
    'meme': 100,
}

# for testing
# FREE_LIMITS = {
#     'text_free': 1,
#     'text': 1,
#     'image': 1,
#     'image_normal': 1,
#     'speak': 1
# }


def handle_rate_limit(requests: List[Request], tier: str, item: str) -> bool:
    request_dict = {
        'text_free': 0,
        'text': 0,
        'image': 0,
        'image_normal': 0,
        'speak': 0
    }

    for request in requests:
        if request.req_type == 'text' and request.quality != 'free':
            request_dict['text'] += 1
        elif request.req_type == 'text' and request.quality == 'free':
            request_dict['text_free'] += 1
        elif request.req_type == 'image' and request.quality != 'normal':
            request_dict['image'] += 1
        elif request.req_type == 'image' and request.quality == 'normal':
            request_dict['image_normal'] += 1
        elif request.req_type == 'speak':
            request_dict['speak'] += 1

    limits = FREE_LIMITS if tier == 'free' else PAID_LIMITS

    for key, value in request_dict.items():
        if value >= limits[key] and key == item:
            return True
    return False


def process_request(engine: Engine, interaction: nextcord.Interaction | nextcord.Message, prompt: str, req_type: str, quality: str) -> tuple[User, Request | None, timedelta | None]:
    '''Takes in a request and processes it, returning a user object, a request object, and a rate limit status, which is true if the user can continue to the next step, false otherwise'''
    discord_user_id = None
    message_id = None
    if isinstance(interaction, nextcord.Interaction):
        discord_user_id = str(interaction.user.id)
        message_id = str(interaction.id)
    elif isinstance(interaction, nextcord.Message):
        discord_user_id = str(interaction.author.id)
        message_id = str(interaction.id)
    else:
        raise TypeError(
            f"Expected interaction or message, got {type(interaction)}")
    if not discord_user_id:
        raise ValueError("discord_user_id cannot be None")
    if not message_id:
        raise ValueError("message_id cannot be None")
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

        # check if we're on a server with a server override
        statement = select(ServerOverrides).where(
            ServerOverrides.guild_id == str(interaction.guild.id))
        server_override = session.exec(statement).first()
        if server_override:
            # if we are, we can ignore rate limits
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
            session.refresh(req)

            return user, req, None

        # here is where rate limits get enforced.
        # get all requests the user has made in the last 24 hours
        statement = select(Request).where(Request.user_id == user.id).where(
            Request.created_at >= datetime.now() - timedelta(hours=24))
        requests = session.exec(statement).all()

        tier = user.payment_status or 'free'

        # not the best way to do this
        # but good enough for now
        item = req_type
        if req_type == 'image' and quality == 'normal':
            item = 'image_normal'
        if req_type == 'text' and quality == 'free':
            item = 'text_free'

        hit_rate_limit = handle_rate_limit(requests, tier, item)
        if hit_rate_limit:
            log.warning(f'User {user.id} ({tier}) hit rate limit for {item}')
            # get the most recent request made by the user within the last 24 hours
            statement = select(Request).where(Request.user_id == user.id).where(
                Request.created_at >= datetime.now() - timedelta(hours=24)).order_by(Request.created_at.desc()).limit(1)
            last_request = session.exec(statement).first()
            # get the time remaining until the user can make another request
            time_remaining = last_request.created_at + \
                timedelta(hours=24) - datetime.now()
            return user, None, time_remaining

        # only add the request if the user hasn't hit the rate limit
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
        session.refresh(req)

        return user, req, None


def process_text_response(session: Session, req: Request, response: str):
    '''Tracks text only responses'''
    text_response = TextResponse(request_id=req.id, response=response)
    session.add(text_response)
    session.commit()
    session.refresh(text_response)
    return text_response
