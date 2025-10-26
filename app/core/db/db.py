import os
from typing import Generator

from sqlmodel import Session, create_engine

dbhost = os.getenv("DB_HOST", "localhost")
dbport = os.getenv("DB_PORT", "5432")
dbname = os.getenv("DB_NAME", "fastapi_db")
postgres_url = f"postgresql://postgres:postgres@{dbhost}:{dbport}/{dbname}"
engine = create_engine(postgres_url, echo=True)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
