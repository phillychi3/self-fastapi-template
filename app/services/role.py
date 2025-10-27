from app.core.service import BaseService
from app.models.role import Role
from app.repositories.role import RoleRepository


class RoleService(BaseService[Role]):
    def __init__(self, repository: RoleRepository):
        super().__init__(repository)
        self.role_repository = repository

    async def get_by_id(self, role_id: int) -> Role:
        return self.role_repository.get_by_id(role_id)

    async def get_by_name(self, name: str) -> Role:
        return self.role_repository.get_by_name(name)
