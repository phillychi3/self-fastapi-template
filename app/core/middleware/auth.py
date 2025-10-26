from starlette.middleware.authentication import AuthenticationBackend
from starlette.requests import HTTPConnection
from app.core.security.jwtutil import JWT
from schemas.auth import AuthUserSchema


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
            AuthUser.id = payload.get("id")
            return True, AuthUser
        except Exception:
            return False, AuthUser
