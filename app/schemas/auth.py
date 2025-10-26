from pydantic import BaseModel, Field


class AuthUserSchema(BaseModel):
    id: int = Field(None, description="user id")
    is_authenticated: bool = False


class LoginRequestSchema(BaseModel):
    username: str = Field(..., description="username or email")
    password: str = Field(..., description="user password")


class LoginSchema(BaseModel):
    access_token: str = Field(..., description="access token")
    refresh_token: str = Field(..., description="refresh token")


class RefreshTokenSchema(BaseModel):
    access_token: str = Field(..., description="new access token")
