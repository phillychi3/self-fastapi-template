from typing import Generic, Type, TypeVar

from sqlmodel import Session, select

from app.core.model import BaseModel

Model = TypeVar("Model", bound="BaseModel")


class BaseRepository(Generic[Model]):
    def __init__(self, model: Type[Model], db_session: Session):
        self.session = db_session
        self.model_class: Type[Model] = model

    def create(self, obj: Model) -> Model:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def get_all(self, limit: int = 100, offset: int = 0) -> list[Model]:
        return self.session.exec(select(self.model_class).limit(limit).offset(offset)).all()

    def delete(self, obj: Model) -> None:
        self.session.delete(obj)
        self.session.commit()
