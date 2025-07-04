import uuid
from datetime import date, datetime, timezone

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, SQLModel


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
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True), default=datetime.now(timezone.utc)
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True), default=datetime.now(timezone.utc)
        )
    )

    def __repr__(self) -> str:
        return (
            f"<Book(uid={self.uid}, title='{self.title}', author='{self.author}', "
            f"published_date={self.published_date}, page_count={self.page_count})>"
        )
