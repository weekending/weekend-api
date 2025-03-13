import pytest

from app.core.settings import get_settings
from .test_band import test_밴드_생성


settings = get_settings()


@pytest.mark.asyncio
async def test_곡_등록(client):
    band = await test_밴드_생성(client)

    data = {
        "band_id": band["id"],
        "title": "밤편지",
        "singer": "야이유",
    }
    response = await client.post("/songs", json=data)
    assert response.status_code == 201
    return response.json()["data"]


@pytest.mark.asyncio
async def test_곡_조회(client):
    song = await test_곡_등록(client)

    response = await client.get(f"/songs/{song['id']}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_곡_제거(client):
    song = await test_곡_등록(client)

    response = await client.delete(f"/songs/{song['id']}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_곡_상태_변경(client):
    song = await test_곡_등록(client)

    data = {"status": "INPROGRESS"}
    response = await client.post(f"/songs/{song['id']}/status", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["data"]["status"] == "INPROGRESS"
