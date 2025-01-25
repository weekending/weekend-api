from functools import lru_cache
import os
from pathlib import Path

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parents[2]


class Settings(BaseSettings):
    """Base Settings"""

    APP_ENV: str

    SECRET_KEY: str

    TIMEZONE: str = "Asia/Seoul"

    DB_URL: str
    SQLALCHEMY_POOL_SIZE: int = 20

    BASE_DOMAIN: str = "https://weekend.miintto.com"

    model_config = ConfigDict(extra="ignore")


@lru_cache()
def get_settings() -> Settings:
    env = os.getenv("APP_ENV", "local")
    return Settings(
        _env_file=(
            BASE_DIR / f".env.{env}",
            BASE_DIR / ".env",
        )
    )
