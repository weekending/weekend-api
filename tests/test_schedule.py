import pytest

from app.core.settings import get_settings
from .test_band import test_밴드_생성


settings = get_settings()


@pytest.mark.asyncio
async def test_일정_등록(client):
    await test_밴드_생성(client)

    data = {
        "day": "2025-01-01",
        "start_time": "12:00",
        "end_time": "14:00",
        "title": "합주",
        "location": "그라운즈 연습실 A1룸",
    }
    response = await client.post("/api/schedule", json=data)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_일정_날짜만_등록(client):
    await test_밴드_생성(client)

    data = {"day": "2025-01-01"}
    response = await client.post("/api/schedule", json=data)
    assert response.status_code == 201
