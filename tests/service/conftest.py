from unittest.mock import AsyncMock

import pytest_asyncio

from app.adapter.outbound.persistence import (
    BandPersistenceAdapter,
    SchedulePersistenceAdapter,
    SongPersistenceAdapter,
    UserBandPersistenceAdapter,
    UserPersistenceAdapter,
)


@pytest_asyncio.fixture
async def band_repo():
    yield AsyncMock(BandPersistenceAdapter)


@pytest_asyncio.fixture
async def schedule_repo():
    yield AsyncMock(SchedulePersistenceAdapter)


@pytest_asyncio.fixture
async def song_repo():
    yield AsyncMock(SongPersistenceAdapter)


@pytest_asyncio.fixture
async def user_band_repo():
    yield AsyncMock(UserBandPersistenceAdapter)


@pytest_asyncio.fixture
async def user_repo():
    yield AsyncMock(UserPersistenceAdapter)
