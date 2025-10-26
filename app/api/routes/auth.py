from fastapi import APIRouter, Body, Depends, HTTPException, status

from app.core.factory import Factory
from app.schemas.auth import LoginRequestSchema, LoginSchema, RefreshTokenSchema
from app.services import LoginService

auth_router = APIRouter()


@auth_router.post("/login", response_model=LoginSchema)
async def login(
    login_request: LoginRequestSchema,
    auth_service: LoginService = Depends(Factory.get_auth_service),
):
    try:
        return await auth_service.login(login_request)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )


@auth_router.post("/refresh-token", response_model=RefreshTokenSchema)
async def refresh_token(
    refresh_token: str = Body(..., embed=True),
    auth_service: LoginService = Depends(Factory.get_auth_service),
):
    try:
        return await auth_service.refresh_tokens(refresh_token)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
