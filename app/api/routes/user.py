from fastapi import APIRouter, Depends
from core.factory import Factory
from services.user import UserService

user_router = APIRouter()


@user_router.get("/me")
async def me(user_service: UserService = Depends(Factory().get_user_service)): ...
