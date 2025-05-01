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
    response = await client.post("/api/schedules", json=data)
    assert response.status_code == 201
    return response.json()["data"]


@pytest.mark.asyncio
async def test_밴드_일정_조회(client):
    schedule = await test_일정_등록(client)

    response = await client.get(
        "/api/schedules", params={"band_id": schedule["id"]}
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_일정_상세_조회(client):
    schedule = await test_일정_등록(client)

    response = await client.get(f"/api/schedules/{schedule['id']}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_일정_날짜만_등록(client):
    band = await test_밴드_생성(client)

    data = {"band_id": band["id"], "title": "일정", "day": "2025-01-01"}
    response = await client.post("/api/schedules", json=data)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_일정_변경(client):
    schedule = await test_일정_등록(client)

    day = "2025-01-02"
    location = "하모닉스 합주실"
    response = await client.patch(
        f"/api/schedules/{schedule['id']}",
        json={"band_id": schedule["id"], "day": day, "location": location},
    )
    assert response.status_code == 200
    result = response.json()
    assert result["data"]["title"] == schedule["title"]
    assert result["data"]["day"] == day
    assert result["data"]["start_time"] == schedule["start_time"]
    assert result["data"]["end_time"] == schedule["end_time"]
    assert result["data"]["location"] == location
    assert result["data"]["memo"] == schedule["memo"]


@pytest.mark.asyncio
async def test_일정_리스트_화면(client):
    response = await client.get("/schedule")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_일정_상세_화면(client):
    schedule = await test_일정_등록(client)

    response = await client.get(f"/schedule/{schedule['id']}")
    assert response.status_code == 200
