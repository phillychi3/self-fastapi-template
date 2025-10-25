from fastapi import Depends, Request
from core.factory import Factory
from services.user import UserService


async def get_me(
    request: Request,
    user_service: UserService = Depends(Factory.get_user_service),
):
    user = await user_service.get_by_id(request.user.id)
    return user
