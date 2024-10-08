from datetime import datetime
from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    discord_id: str = Field(default=None, unique=True, nullable=False)
    payment_status: Optional[str] = Field(default=None)
    request: List["Request"] = Relationship(back_populates="user")
    created_at: datetime = Field(default=datetime.now(), nullable=False)


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
    feedback: List["Feedback"] = Relationship(back_populates="request")
    textresponse: List["TextResponse"] = Relationship(back_populates="request")


class Overrides(SQLModel, table=True):
    '''Used to allow certain servers to ignore rate limits. Eventually this will be replaced with a more robust system. For now if they're in the table, they can ignore rate limits.'''
    id: Optional[int] = Field(default=None, primary_key=True)
    guild_id: Optional[str] = Field(default=None, unique=True, nullable=True)
    # optional, overrides guild_id if both are present
    channel_id: Optional[str] = Field(default=None, nullable=True)
    payment_status: Optional[str] = Field(default=None)
    assistant_id: Optional[str] = Field(default=None, nullable=True)
    intro_message: Optional[str] = Field(default=None, nullable=True)
    athena_namespace: Optional[str] = Field(default=None, nullable=True)
    quickchat_system_prompt: Optional[str] = Field(default=None, nullable=True)


class Thread(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    request_id: int = Field(default=None, foreign_key="request.id")
    request: Optional[Request] = Relationship(back_populates="thread")
    openai_id: str = Field(default=None, nullable=False)
    discord_id: str = Field(default=None, nullable=False)
    assistant_id: str = Field(default=None, nullable=False)  # assistant id
    last_run_id: str = Field(default=None, nullable=True)

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
    size: int = Field(default=0, nullable=False)  # in bytes

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
    summaryreplies: List["SummaryReplies"] = Relationship(
        back_populates="summary")
    feedback: List["Feedback"] = Relationship(back_populates="summary")

    @property
    def user(self):
        return self.request.user

    @property
    def created_at(self):
        return self.request.created_at


class SummaryReplies(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    summary_id: int = Field(default=None, foreign_key="summary.id")
    summary: Optional[Summary] = Relationship(back_populates="summaryreplies")
    original_message_id: str = Field(default=None, nullable=False)
    reply_message_id: str = Field(default=None, nullable=False)


class Feedback(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    request_id: int = Field(default=None, foreign_key="request.id")
    request: Optional[Request] = Relationship(back_populates="feedback")
    summary_id: Optional[int] = Field(default=None, foreign_key="summary.id")
    summary: Optional[Summary] = Relationship(back_populates="feedback")
    feedback: str = Field(default=None)
    rating: int = Field(default=0, nullable=False)
    created_at: datetime = Field(default=datetime.now(), nullable=False)
    # user that gave the feedback. Not necessarily the user that made the request
    user_id: int = Field(default=None, foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="feedback")

    @property
    def user(self):
        return self.request.user

    @property
    def created_at(self):
        return self.request.created_at


class TextResponse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    request_id: int = Field(default=None, foreign_key="request.id")
    request: Optional[Request] = Relationship(back_populates="textresponse")
    response: str = Field(default=None, nullable=False)
    # useful for looking at response times. Check the difference between created_at and request.created_at
    created_at: datetime = Field(default=datetime.now(), nullable=False)
