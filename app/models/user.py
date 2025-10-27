from typing import Optional

from sqlmodel import Field, Relationship

from app.core.model import BaseModel
from app.core.security.pwdhash import hash_password, verify_password


class User(BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    role_id: Optional[int] = Field(default=None, foreign_key="role.id")

    role: Optional["Role"] = Relationship(back_populates="users")

    def set_password(self, password: str):
        self.password_hash = hash_password(password)

    def verify_password(self, password: str) -> bool:
        return verify_password(password, self.password_hash)
