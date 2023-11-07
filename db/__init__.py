import os

from sqlmodel import create_engine, SQLModel
from dotenv import load_dotenv

from db.models import *

load_dotenv()


def new_engine(uri: str = "sqlite:///./sam.db", echo=False):
    engine = create_engine(uri, echo=echo)
    SQLModel.metadata.create_all(engine)
    return engine


engine = new_engine(os.getenv("DB_URI", "sqlite:///./sam.db"),
                    os.getenv("DB_ECHO") == "true")
