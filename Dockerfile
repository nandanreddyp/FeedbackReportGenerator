FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY . /app

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root

RUN apt-get update && \
    apt-get install -y gcc libpq-dev \
    libcairo2 libcairo2-dev libpangocairo-1.0-0 weasyprint && \
    apt clean && \
    rm -rf /var/cache/apt/*