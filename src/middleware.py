import logging
import time

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.requests import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger("uvicorn.access")
logger.disabled = True


def register_middleware(app: FastAPI):

    @app.middleware("http")
    async def custom_logging(request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)
        processing_time = time.time() - start_time

        message = f"{request.client.host}:{request.client.port} - {request.method} - {request.url.path} - {response.status_code} completed after {processing_time}s"

        print(message)
        return response

    # @app.middleware("http")
    # async def authorization(request: Request, call_next):
    #     # exclude the login and signup routes
    #     excluded_paths = ["/api/v1/auth/signup", "/api/v1/auth/login"]

    #     if request.url.path in excluded_paths:
    #         return await call_next(request)

    #     if not "Authorization" in request.headers:
    #         return JSONResponse(
    #             content={
    #                 "message": "Not Authenticated",
    #                 "resolution": "Please provide the right credentials to proceed",
    #             },
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #         )
    #     response = await call_next(request)
    #     return response

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=[
            "localhost",
            "127.0.0.1",
            "bookly-api-hab5.onrender.com",
            "0.0.0.0",
        ],
    )
