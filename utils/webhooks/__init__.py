import os

import httpx
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv('WEBHOOK')


def format_error_webhook(error: str, command: str, channel_id: str, message_id: str, user_id: str, content: str) -> str:
    if len(error) > 600:
        error = error[:597] + '...'
    if len(content) > 600:
        content = content[:597] + '...'
    return f'Error: {error}\nCommand: {command} \nChannel: {channel_id} \nMessage: {message_id} \nUser: {user_id} \nContent: {content}'


def format_feedback_webhook(user_id: str, message_id: str, channel_id: str, feedback: str) -> str:
    if len(feedback) > 1000:
        feedback = feedback[:997] + '...'
    return f'User {user_id} gave {feedback} feedback on message \n{message_id} in channel \n{channel_id}'


async def send_webhook(msg: str) -> None:
    async with httpx.AsyncClient() as client:
        await client.post(WEBHOOK_URL, json={
            'content': msg
        })


async def send_error_webhook(error: str, command: str, channel_id: str, message_id: str, user_id: str, content: str) -> None:
    await send_webhook(format_error_webhook(error, command, channel_id, message_id, user_id, content))


async def send_feedback_webhook(user_id: str, message_id: str, channel_id: str, feedback: str) -> None:
    await send_webhook(format_feedback_webhook(user_id, message_id, channel_id, feedback))
