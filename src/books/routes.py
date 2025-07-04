from fastapi import APIRouter, status, Depends
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel
from src.db.main import get_session
from typing import List
from src.books.models import Book

book_router = APIRouter()


@book_router.get("/", response_model=List[Book])
async def read_books():
    """Read all books"""
    return books


@book_router.get("/{book_id}")
async def read_book(book_id: int):
    """Read a book"""
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}


@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    """Create a new book"""
    books.append(book)
    return book


@book_router.patch("/{book_id}")
async def update_book(book_id: int, update_data: BookUpdateModel):
    """ "update book"""
    for book in books:
        if book["id"] == book_id:
            book["title"] = update_data.title
            book["author"] = update_data.author
            book["publisher"] = update_data.publisher
            book["page_count"] = update_data.page_count
            book["language"] = update_data.language
            return book
    return {"message": "Book not found"}


@book_router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: int):
    """delete a book"""
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return book
    return {"message": "Book not found"}
