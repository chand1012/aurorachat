import io
from datetime import datetime

from sqlmodel import Session
import nextcord
from nextcord.ext import commands
from openai import OpenAI

from db.models import UserUploads, User, Request
from utils.file_buffer import FileBuffer

SUPPORTED_EXTENSIONS = ['c', 'cpp', 'csv', 'docx', 'html', 'java', 'json', 'md', 'pdf', 'php', 'pptx',
                        'py', 'rb', 'tex', 'txt', 'css', 'js', 'tar', 'ts', 'xlsx', 'xml', 'zip']


async def process_upload(session: Session, openai: OpenAI, attachment: nextcord.Attachment, user: User, request: Request) -> UserUploads | None:
    if attachment.size > 8000000:
        return None
    content = await attachment.read()
    file_name = attachment.filename
    if not file_name.endswith(tuple(SUPPORTED_EXTENSIONS)):
        raise commands.CommandError(
            f"I cannot understand files with the extension '{file_name.split('.')[-1]}'. Here is a list of what I can understand: {', '.join(SUPPORTED_EXTENSIONS)}")
    buf = FileBuffer(content, file_name)
    buf.seek(0)
    resp = openai.files.create(
        file=buf,
        purpose="assistants",
    )
    upload = UserUploads(
        user_id=user.id,
        req_id=request.id,
        content_type=attachment.content_type,
        openai_id=resp.id,
        created_at=datetime.fromtimestamp(resp.created_at),
        name=file_name
    )
    session.add(upload)
    session.commit()
    return upload
