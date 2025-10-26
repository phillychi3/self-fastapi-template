from app.core.service import BaseService
from app.models.user import User
from app.repositories import UserRepository


class UserService(BaseService[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)
        self.user_repository = repository

    async def get_by_id(self, user_id: int) -> User:
        return self.user_repository.get_by_id(user_id)

    async def get_by_username(self, username: str) -> User:
        return self.user_repository.get_by_username(username)

    async def get_by_email(self, email: str) -> User:
        return self.user_repository.get_by_email(email)
