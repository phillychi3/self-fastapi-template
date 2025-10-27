from typing import Optional, List
from sqlmodel import Field, Relationship
from app.core.model import BaseModel


class Role(BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    description: Optional[str] = None

    users: List["User"] = Relationship(back_populates="role")
