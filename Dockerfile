###############################################################################
# BUILD IMAGE                                                                 #
###############################################################################
FROM python:3.12-slim AS build

RUN apt-get -y update \
    && apt-get install -y \
    libpq-dev \
    gcc \
    && pip install uv

WORKDIR /usr/src

COPY uv.lock pyproject.toml /usr/src/

RUN uv venv --python 3.12 .venv \
    && PATH="/usr/src/.venv/bin:$PATH" \
    uv sync --no-dev

###############################################################################
# RUNTIME IMAGE                                                               #
###############################################################################
FROM python:3.12-slim

ENV PATH="/usr/src/.venv/bin:$PATH"

EXPOSE 8000

WORKDIR /usr/src

RUN apt-get -y update \
    && apt-get install -y --no-install-recommends \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /usr/src/.venv /usr/src/.venv

COPY ./app /usr/src/app
COPY ./static /usr/src/static

CMD ["gunicorn", "--bind=0.0.0.0:8000", "--workers=5", "--worker-class=uvicorn.workers.UvicornWorker", "app.asgi:app"]
