from fastapi import Depends
from sqlmodel import Session

from app.core.db import get_db
from app.repositories import UserRepository
from app.services import LoginService, UserService


class Factory:
    @staticmethod
    def get_user_service(db: Session = Depends(get_db)) -> UserService:
        user_repository = UserRepository(db_session=db)
        user_service = UserService(repository=user_repository)
        return user_service

    @staticmethod
    def get_auth_service(db: Session = Depends(get_db)) -> LoginService:
        user_repository = UserRepository(db_session=db)
        auth_service = LoginService(repository=user_repository)
        return auth_service
