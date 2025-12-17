FROM python:3.14.0

WORKDIR /actions_test

COPY app/ app/
COPY tests/ tests/
COPY Makefile .
COPY pyproject.toml .
COPY uv.lock .
COPY requirements.txt .

RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install uv \
    && python3 -m uv sync
