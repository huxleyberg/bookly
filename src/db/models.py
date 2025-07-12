import uuid
from datetime import date, datetime, timezone
from typing import List, Optional

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, Relationship, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    username: str
    email: str
    first_name: str
    last_name: str
    role: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False, server_default="user")
    )
    is_verified: bool = Field(default=False)
    password_hash: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False), exclude=True
    )
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    books: List["Book"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )

    def __repr__(self):
        return f"<User {self.username}>"


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
    user_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="users.uid")
    user: Optional["User"] = Relationship(back_populates="books")
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
