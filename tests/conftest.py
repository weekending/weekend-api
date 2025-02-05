import asyncio

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from app.models.base import BaseModel

try:
    from app.asgi import app
    from app.core.database import db
except ImportError:
    raise


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def setup_db():
    async with db.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield
    async with db.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def client(setup_db) -> AsyncClient:
    async with AsyncClient(
        base_url="http://test.miintto.com", transport=ASGITransport(app)
    ) as async_client:
        yield async_client
