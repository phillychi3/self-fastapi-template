from fastapi import APIRouter, Depends

from app.core.dependencies.me import get_me
from app.models.user import User

user_router = APIRouter()


@user_router.get("/me")
async def me(user: User = Depends(get_me)):
    return user
