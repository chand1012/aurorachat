import asyncio

from sqlmodel import Session
import nextcord
from nextcord.ext import commands
from openai import OpenAI
from loguru import logger as log

from db.models import Thread
from utils import split_messages

# TODO - fix runs not being proper handled (they are not being deleted on error)


async def process_thread(session: Session, o: OpenAI, channel: nextcord.PartialMessageable, db_thread: Thread, content: str, files: list[str] = []):
    # if there are more than 10 files, forget the oldest (first ones)
    if len(files) > 10:
        files = files[-10:]
    new_message = o.beta.threads.messages.create(
        thread_id=db_thread.openai_id,
        role="user",
        content=content,
        file_ids=files
    )
    run = o.beta.threads.runs.create(
        thread_id=db_thread.openai_id,
        assistant_id=db_thread.assistant_id,
    )
    db_thread.last_run_id = run.id
    session.commit()
    while run.status != "completed":
        run = o.beta.threads.runs.retrieve(
            thread_id=db_thread.openai_id,
            run_id=db_thread.last_run_id
        )
        match run.status:
            case "completed":
                break
            case "requires_action":
                raise NotImplementedError(
                    "Requires action is not implemented yet."
                )
            case "failed":
                raise commands.CommandError(
                    f"Error processing request: run failed. Please report with the run id: {run.id}")
            case "cancelling":
                await channel.send("Cancelling request...")
                return
            case "cancelled":
                await channel.send("Request cancelled.")
                return
            case "expired":
                raise commands.CommandError(
                    f"Error processing request: run expired. Please report with the run id: {run.id}")
            case _:
                await asyncio.sleep(1)
    messages = o.beta.threads.messages.list(
        thread_id=db_thread.openai_id,
    )
    # these need to be reversed because the messages are in reverse order
    message_responses = []
    for message in messages:
        if message.id == new_message.id:
            break
        for c in message.content:
            if c.type == "image_file":
                # not implemented, print warning and skip
                log.warning(
                    f"Run {run.id} has an image file. This is not implemented yet.")
                continue
            elif c.type == "text":
                response_text = c.text.value
                if len(response_text) > 2000:
                    # split until the message is less than 2000 characters
                    responses = split_messages(response_text)
                    for response in responses:
                        message_responses.append(response)
                else:
                    message_responses.append(response_text)
            else:
                log.error(f"Unknown message type: {c.type}")
                # skip
                continue
    message_responses.reverse()
    for response in message_responses:
        await channel.send(response)
