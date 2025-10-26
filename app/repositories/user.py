from core.repository import BaseRepository
from models.user import User
from sqlmodel import select


class UserRepository(BaseRepository[User]):
    def __init__(self, model, db_session):
        super().__init__(model, db_session)

    def get_by_id(self, user_id: int) -> User:
        statement = select(User).where(User.id == user_id)
        return self.session.exec(statement).first()
