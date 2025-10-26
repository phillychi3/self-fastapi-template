from fastapi import APIRouter

from .auth import auth_router
from .user import user_router
from .worker import worker_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(worker_router, prefix="/worker", tags=["worker"])


__all__ = ["api_router"]
