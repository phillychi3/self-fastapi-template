from user import user_router
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(user_router, prefix="/user", tags=["user"])


__all__ = ["api_router"]
