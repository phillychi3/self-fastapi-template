from fastapi import APIRouter, Depends
from core.factory import Factory
from services import LoginService
from schemas.auth import LoginSchema, RefreshTokenSchema

auth_router = APIRouter()


@auth_router.get("/login", response_model=LoginSchema)
async def login(auth_service: LoginService = Depends(Factory().get_auth_service)):
    return await auth_service.login()


@auth_router.get("/refresh-token", response_model=RefreshTokenSchema)
async def refresh_token(
    auth_service: LoginService = Depends(Factory().get_auth_service),
):
    return await auth_service.refresh_tokens()
