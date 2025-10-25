from core.service import BaseService
from models.user import User


class UserService(BaseService[User]):
    def get_by_id(self, user_id: int) -> User:
        return self.get_by_id(user_id)
