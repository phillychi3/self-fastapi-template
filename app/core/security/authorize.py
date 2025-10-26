import datetime
from enum import Enum

from app.core.security.jwtutil import JWT


class TokenType(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"


def create_access_token(user_id: int) -> str:
    return JWT().encode(
        {
            "id": user_id,
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=15),
            "type": TokenType.ACCESS,
        }
    )


def create_refresh_token(user_id: int) -> str:
    return JWT().encode(
        {
            "id": user_id,
            "exp": datetime.datetime.now() + datetime.timedelta(days=7),
            "type": TokenType.REFRESH,
        }
    )


def verify_token(token: str, expected_type: TokenType) -> dict:
    payload = JWT().decode(token)
    if payload.get("type") != str(expected_type):
        raise ValueError("Invalid token type")
    return payload
