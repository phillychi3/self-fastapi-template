from typing import Optional
from sqlmodel import Field
from core.model import BaseModel


class User(BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    password_hash: str
