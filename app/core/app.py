from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from jwt import PyJWTError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.api.routes import api_router
from app.core.middleware.auth import Auth
from app.core.middleware.exception import (
    exception_middleware,
    http_exception_handler,
    jwt_exception_handler,
    validation_exception_handler,
)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="FastAPI",
        description="FastAPI",
        version="1.0.0",
        docs_url="/docs",
    )

    app_.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app_.add_exception_handler(RequestValidationError, validation_exception_handler)
    app_.add_exception_handler(PyJWTError, jwt_exception_handler)

    app_.middleware("http")(exception_middleware)

    app_.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app_.add_middleware(
        AuthenticationMiddleware,
        backend=Auth(),
        on_error=lambda conn, exc: None,
    )
    app_.include_router(api_router, prefix="/api")
    return app_


app = create_app()
