from fastapi import Depends
from sqlmodel import Session

from app.core.db import get_db
from app.repositories import UserRepository, RoleRepository
from app.services import LoginService, UserService, RoleService


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

    @staticmethod
    def get_role_service(db: Session = Depends(get_db)) -> RoleService:
        role_repository = RoleRepository(db_session=db)
        role_service = RoleService(repository=role_repository)
        return role_service
