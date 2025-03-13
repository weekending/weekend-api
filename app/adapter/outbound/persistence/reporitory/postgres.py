from asyncio import TimeoutError, current_task, open_connection, wait_for
from contextlib import asynccontextmanager
import logging

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from app.core.settings import get_settings

logger = logging.getLogger(__name__)

settings = get_settings()


class PostgresConnection:
    def __init__(self) -> None:
        self._engine = create_async_engine(
            url=settings.DB_URL,
            pool_size=settings.SQLALCHEMY_POOL_SIZE,
        )
        self._scoped_session = async_scoped_session(
            session_factory=async_sessionmaker(
                bind=self._engine,
                autocommit=False,
                autoflush=False,
                expire_on_commit=False,
            ),
            scopefunc=current_task,
        )

    @property
    def engine(self) -> AsyncEngine:
        return self._engine

    async def check_connection(self):
        try:
            await wait_for(
                open_connection(
                    self.engine.url.host,
                    self.engine.url.port,
                    limit=1,
                ),
                timeout=1,
            )
            logger.info(f"PostgreSQL OK - {self.engine.url.host}")
        except TimeoutError:
            raise TimeoutError("Cannot connect to PostgreSQL.")

    async def dispose_connection(self):
        await self.engine.dispose()

    async def get_session(self) -> AsyncSession:
        async with self._scoped_session() as session:
            try:
                yield session
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await self._scoped_session.remove()
