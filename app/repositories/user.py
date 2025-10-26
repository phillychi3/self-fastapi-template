from sqlmodel import select

from app.core.repository import BaseRepository
from app.models.user import User


class UserRepository(BaseRepository[User]):
    def __init__(self, db_session):
        super().__init__(model=User, db_session=db_session)

    def get_by_id(self, user_id: int) -> User:
        statement = select(User).where(User.id == user_id)
        return self.session.exec(statement).first()

    def get_by_username(self, username: str) -> User:
        statement = select(User).where(User.username == username)
        return self.session.exec(statement).first()

    def get_by_email(self, email: str) -> User:
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()
