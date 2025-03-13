import pytest

from app.core.settings import get_settings
from .test_band import test_밴드_생성


settings = get_settings()


@pytest.mark.asyncio
async def test_일정_등록(client):
    band = await test_밴드_생성(client)

    data = {
        "band_id": band["id"],
        "day": "2025-01-01",
        "start_time": "12:00",
        "end_time": "14:00",
        "title": "합주",
        "location": "그라운즈 연습실 A1룸",
    }
    response = await client.post("/schedules", json=data)
    assert response.status_code == 201
    return response.json()["data"]


@pytest.mark.asyncio
async def test_밴드_일정_조회(client):
    schedule = await test_일정_등록(client)

    response = await client.get(
        "/schedules", params={"band_id": schedule["id"]}
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_일정_상세_조회(client):
    schedule = await test_일정_등록(client)

    response = await client.get(f"/schedules/{schedule['id']}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_일정_날짜만_등록(client):
    band = await test_밴드_생성(client)

    data = {"band_id": band["id"], "day": "2025-01-01"}
    response = await client.post("/schedules", json=data)
    assert response.status_code == 201
