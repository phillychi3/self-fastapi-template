from pydantic import BaseModel, Field


class AuthUserSchema(BaseModel):
    id: int = Field(..., description="user id")
