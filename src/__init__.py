"""app main entry point"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from src.books.routes import book_router
from src.db.main import init_db


@asynccontextmanager
async def life_span(_app: FastAPI):
    """books async context manager"""
    print("server is starting ..... ")
    await init_db()
    yield
    print("server has been stopped.")


VERSION = "v1"

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=VERSION,
    lifespan=life_span,
)


app.include_router(book_router, prefix=f"/api/{VERSION}/books", tags=["books"])
