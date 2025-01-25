import os


os.environ.setdefault("APP_ENV", "test")
os.environ.setdefault("SECRET_KEY", "test")
os.environ.setdefault(
    "DB_URL", "postgresql+asyncpg://testuser:root@127.0.0.1:5432/db"
)
