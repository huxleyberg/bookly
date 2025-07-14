import debugpy
from fastapi import FastAPI

from middleware import register_middleware
from src.auth.routers import auth_router
from src.books.routes import book_router
from src.errors import register_all_errors
from src.reviews.routes import review_router
from src.tags.routes import tags_router

VERSION = "v1"


# debugpy.listen(("localhost", 5678))
# print("Debugger listening on port 5678")

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=VERSION,
    docs_url=f"/api/{VERSION}/docs",
    redoc_url=f"/api/{VERSION}/redoc",
    contact={"email": "huxleyberg@live.com"},
)

register_all_errors(app)

register_middleware(app)

app.include_router(auth_router, prefix=f"/api/{VERSION}/auth", tags=["auth"])
app.include_router(book_router, prefix=f"/api/{VERSION}/books", tags=["books"])
app.include_router(review_router, prefix=f"/api/{VERSION}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"/api/{VERSION}/tags", tags=["tags"])
