from typing import Generic, TypeVar

from app.core.repository import BaseRepository

Model = TypeVar("Model")


class BaseService(Generic[Model]):
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def create(self, obj: Model) -> Model:
        return self.repository.create(obj)

    def get_all(self, limit: int = 100, offset: int = 0) -> list[Model]:
        return self.repository.get_all(limit=limit, offset=offset)

    def delete(self, obj: Model) -> None:
        self.repository.delete(obj)
