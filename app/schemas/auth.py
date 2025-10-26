from pydantic import BaseModel, Field


class AuthUserSchema(BaseModel):
    id: int = Field(..., description="user id")


class LoginSchema(BaseModel):
    access_token: str = Field(..., description="access token")
    refresh_token: str = Field(..., description="refresh token")


class RefreshTokenSchema(BaseModel):
    access_token: str = Field(..., description="new access token")
