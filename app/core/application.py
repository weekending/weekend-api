from logging.config import DictConfigurator

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.core.openapi import DESCRIPTION
from app.core.database import db
from app.core.logging.config import logging_config
from app.core.middlewares.logging import LoggingMiddleware
from app.core.settings import get_settings
from app.routes import router

settings = get_settings()


def create_app() -> FastAPI:
    app = FastAPI(
        title="윅엔드",
        description="밴드 연습곡 관리를 위한 어플리케이션" + DESCRIPTION,
        docs_url=None,
        redoc_url=None,
    )

    app.include_router(router)

    # Logging
    DictConfigurator(logging_config).configure()

    # Middlewares
    app.add_middleware(LoggingMiddleware)

    # Database
    app.add_event_handler("startup", db.check_connection)
    app.add_event_handler("shutdown", db.dispose_connection)

    # Static
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app
