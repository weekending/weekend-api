import os

from app.core.settings import BASE_DIR


LOG_DIR = os.path.join(BASE_DIR, "logs/")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "[%(asctime)s] - [%(levelname)s] - %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": f"{LOG_DIR}/debug.log",
        },
    },
    "loggers": {
        "fastapi.request": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
        "sqlalchemy.engine": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "app": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
