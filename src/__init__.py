import debugpy
from fastapi import FastAPI

from src.auth.routers import auth_router
from src.books.routes import book_router

VERSION = "v1"


debugpy.listen(("localhost", 5678))
print("Debugger listening on port 5678")

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=VERSION,
)

app.include_router(auth_router, prefix=f"/api/{VERSION}/auth", tags=["auth"])
app.include_router(book_router, prefix=f"/api/{VERSION}/books", tags=["books"])
