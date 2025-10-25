from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
from middleware.auth import Auth


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="FastAPI",
        description="FastAPI",
        version="1.0.0",
    )
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
    )
    return app_


app = create_app()
