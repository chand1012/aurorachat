from datetime import datetime

from sqlmodel import Session
import nextcord
from nextcord.ext import commands
from openai import OpenAI

from db.models import UserUploads, User, Request

from utils.file_buffer import FileBuffer

# flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm
AUDIO_FILE_EXT = ['flac', 'mp3', 'mp4', 'mpeg',
                  'mpga', 'm4a', 'ogg', 'wav', 'webm']


async def process_audio(session: Session, o: OpenAI, attachment: nextcord.Attachment, user: User, request: Request) -> UserUploads | None:
    if attachment.size > 8000000:
        return None
    if not attachment.filename.endswith(tuple(AUDIO_FILE_EXT)):
        raise commands.CommandError(
            f"I cannot understand audio files with the extension '{attachment.filename.split('.')[-1]}'. Here is a list of what audio I can understand: {', '.join(AUDIO_FILE_EXT)}")
    content = await attachment.read()
    buf = FileBuffer(content, attachment.filename)
    transcript = o.audio.transcriptions.create(
        model="whisper-1",
        file=buf,
    )
    new_filename = attachment.filename.replace(
        attachment.filename.split('.')[-1], 'txt')
    buf = FileBuffer(transcript.text.encode(), new_filename)
    resp = o.files.create(
        file=buf,
        purpose="assistants",
    )
    upload = UserUploads(
        user_id=user.id,
        req_id=request.id,
        content_type=attachment.content_type,
        openai_id=resp.id,
        created_at=datetime.fromtimestamp(resp.created_at),
        name=new_filename
    )
    session.add(upload)
    session.commit()
    return upload
