import uuid
from datetime import date, datetime, Column, Field
from sqlmodel import SQLModel
import sqlalchemy.dialects.postgresql as pg


class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self) -> str:
        return (
            f"<Book(uid={self.uid}, title='{self.title}', author='{self.author}', "
            f"published_date={self.published_date}, page_count={self.page_count})>"
        )
