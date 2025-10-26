from core.service import BaseService
from models.user import User
from core.security.authorize import (
    TokenType,
    create_access_token,
    create_refresh_token,
    verify_token,
)
from schemas.auth import LoginSchema, RefreshTokenSchema


class LoginService(BaseService[User]):
    def __init__(self, repository):
        super().__init__(repository)

    def login(self, user_id: int) -> LoginSchema:
        access_token = create_access_token(user_id)
        refresh_token = create_refresh_token(user_id)
        return LoginSchema(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    def refresh_tokens(self, refresh_token: str) -> RefreshTokenSchema:
        payload = verify_token(refresh_token, TokenType.REFRESH)
        user_id = payload.get("id")
        return RefreshTokenSchema(
            access_token=create_access_token(user_id),
        )
