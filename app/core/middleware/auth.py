from starlette.middleware.authentication import AuthenticationBackend
from starlette.requests import HTTPConnection

from app.core.security.authorize import TokenType
from app.core.security.jwtutil import JWT
from app.schemas.auth import AuthUserSchema


class Auth(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection) -> tuple[bool, AuthUserSchema]:
        AuthUser = AuthUserSchema()
        if "Authorization" not in conn.headers:
            return False, AuthUser

        auth = conn.headers["Authorization"]
        if not auth:
            return False, AuthUser
        try:
            scheme, token = auth.split()
            if scheme.lower() != "bearer":
                return False, AuthUser
            payload = JWT.decode(token)
            if payload.get("type") != TokenType.ACCESS.value:
                return False, AuthUser
            AuthUser.id = payload.get("id")
            AuthUser.is_authenticated = True
            return True, AuthUser
        except Exception:
            return False, AuthUser
