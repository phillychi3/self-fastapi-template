from sqlmodel import select
from app.core.repository import BaseRepository
from app.models.role import Role


class RoleRepository(BaseRepository[Role]):
    def __init__(self, db_session):
        super().__init__(model=Role, db_session=db_session)

    def get_by_id(self, role_id: int) -> Role:
        statement = select(Role).where(Role.id == role_id)
        return self.session.exec(statement).first()

    def get_by_name(self, name: str) -> Role:
        statement = select(Role).where(Role.name == name)
        return self.session.exec(statement).first()
