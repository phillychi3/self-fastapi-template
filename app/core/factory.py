from services import UserService, LoginService
from repositories import UserRepository
from sqlmodel import Session
from fastapi import Depends
from core.db import get_db


class Factory:
    def get_user_service(self, db: Session = Depends(get_db)) -> UserService:
        user_repository = UserRepository(db_session=db)
        user_service = UserService(repository=user_repository)
        return user_service

    def get_auth_service(self, db: Session = Depends(get_db)) -> LoginService:
        user_repository = UserRepository(db_session=db)
        auth_service = LoginService(repository=user_repository)
        return auth_service
