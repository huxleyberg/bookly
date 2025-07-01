from pydantic import BaseModel
import uuid
from datetime import date, datetime


class BookSchema(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    update_at: datetime


class BookUpdateSchema(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
