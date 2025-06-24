FROM python:3.12-slim


RUN apt-get update && apt-get install -y curl build-essential && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app


COPY pyproject.toml poetry.lock* README.md ./


RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi


COPY ./app ./app


ENV PYTHONPATH=/app


EXPOSE 8000


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
