import jwt
import os


class JWT:
    secret_key = os.getenv("JWT_SECRET_KEY")

    @staticmethod
    def encode(payload: dict) -> str:
        return jwt.encode(payload, JWT.secret_key, algorithm="HS256")

    @staticmethod
    def decode(token: str) -> dict:
        return jwt.decode(token, JWT.secret_key, algorithms=["HS256"])
