from app.core.security.authorize import TokenType, create_access_token, create_refresh_token, verify_token
from app.core.service import BaseService
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.auth import LoginRequestSchema, LoginSchema, RefreshTokenSchema


class LoginService(BaseService[User]):
    def __init__(self, repository: UserRepository):
        super().__init__(repository)
        self.user_repository: UserRepository = repository

    async def login(self, login_request: LoginRequestSchema) -> LoginSchema:
        if "@" in login_request.username:
            user = self.user_repository.get_by_email(login_request.username)
        else:
            user = self.user_repository.get_by_username(login_request.username)
        if not user or not user.verify_password(login_request.password):
            raise ValueError("Invalid username or password")
        user_id = user.id
        access_token = create_access_token(user_id)
        refresh_token = create_refresh_token(user_id)
        return LoginSchema(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    async def refresh_tokens(self, refresh_token: str) -> RefreshTokenSchema:
        try:
            payload = verify_token(refresh_token, TokenType.REFRESH)
            user_id = payload.get("id")
            return RefreshTokenSchema(
                access_token=create_access_token(user_id),
            )
        except Exception as e:
            raise ValueError("Invalid or expired refresh token") from e
