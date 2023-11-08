import io
from datetime import datetime

from sqlmodel import Session
import nextcord
from openai import OpenAI

from db.models import UserUploads, User, Request


async def process_upload(session: Session, openai: OpenAI, attachment: nextcord.Attachment, user: User, request: Request) -> UserUploads | None:
    if attachment.size > 8000000:
        return None
    content = await attachment.read()
    buf = io.BytesIO(content)
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
        created_at=datetime.fromtimestamp(resp.created_at)
    )
    session.add(upload)
    session.commit()
    return upload
