import os

from sqlmodel import create_engine, SQLModel
from dotenv import load_dotenv

from db.models import *

load_dotenv()

DB_URI = os.getenv("DATABASE_URL", "sqlite:///./sam.db")
DB_ECHO = os.getenv("DB_ECHO") == "true"


def new_engine(uri=DB_URI, echo=DB_ECHO):
    engine = create_engine(uri, echo=echo)
    SQLModel.metadata.create_all(engine)
    return engine
