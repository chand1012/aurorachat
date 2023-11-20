from datetime import datetime
from typing import Optional, List, Literal

from sqlmodel import Field, SQLModel, Relationship, JSON, Column


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    discord_id: str = Field(default=None, unique=True, nullable=False)
    payment_status: Optional[str] = Field(default=None)
    request: List["Request"] = Relationship(back_populates="user")


class Request(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="request")
    prompt: str = Field(default=None)
    req_type: str = Field(default='text')  # text, image, etc
    quality: str = Field(default='normal')  # normal, better, best
    created_at: datetime = Field(default=datetime.now())
    message_id: str = Field(default=None, nullable=False)
    guild_id: str = Field(default=None, nullable=False)
    channel_id: str = Field(default=None, nullable=False)
    # single thread per request at most
    thread: Optional["Thread"] = Relationship(back_populates="request")
    # however there can be multiple user uploads per request
    useruploads: List["UserUploads"] = Relationship(back_populates="request")
    generatedfiles: List["GeneratedFiles"] = Relationship(
        back_populates="request")
    summary: Optional["Summary"] = Relationship(back_populates="request")


class Thread(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    request_id: int = Field(default=None, foreign_key="request.id")
    request: Optional[Request] = Relationship(back_populates="thread")
    openai_id: str = Field(default=None, nullable=False)
    discord_id: str = Field(default=None, nullable=False)
    assistant_id: str = Field(default=None, nullable=False)  # assistant id
    last_run_id: str = Field(default=None, nullable=False)

    @property
    def user(self):
        return self.request.user

    @property
    def created_at(self):
        return self.request.created_at


# Note: We need to make sure that files get deleted eventually. 24 hours maybe?
class UserUploads(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(
        default=None, nullable=False)  # get from openai api
    req_id: int = Field(default=None, foreign_key="request.id")
    request: Optional[Request] = Relationship(back_populates="useruploads")
    content_type: str = Field(default=None, nullable=False)
    openai_id: str = Field(default=None, nullable=False)
    name: Optional[str] = Field(default=None)

    @property
    def user(self):
        return self.request.user


class GeneratedFiles(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    req_id: int = Field(default=None, foreign_key="request.id")
    request: Optional[Request] = Relationship(back_populates="generatedfiles")
    file_type: str = Field(
        default=None, nullable=False)  # image, audio, etc

    @property
    def user(self):
        return self.request.user

    @property
    def created_at(self):
        return self.request.created_at


class Summary(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    req_id: int = Field(default=None, foreign_key="request.id")
    request: Optional[Request] = Relationship(back_populates="summary")
    summary: str = Field(default=None, nullable=False)
    transcript: str = Field(default=None)
    url: str = Field(default=None)
    # only applicable if the summary is a youtube video
    yt_id: str = Field(default=None)

    @property
    def user(self):
        return self.request.user

    @property
    def created_at(self):
        return self.request.created_at
