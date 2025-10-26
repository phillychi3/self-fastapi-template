FROM python:3.13-bookworm as build

RUN pip install poetry==2.1.4

ENV POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    VIRTUAL_ENV=/app/.venv

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create true \
    && poetry install && rm -rf $POETRY_CACHE_DIR

FROM python:3.13-slim-bookworm as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /app

COPY ./app ./app
COPY ./worker ./worker

EXPOSE 8000

CMD ["uvicorn", "app.core.app:app", "--host", "0.0.0.0", "--port", "8000"]