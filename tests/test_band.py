import pytest

from app.core.settings import get_settings
from .test_auth import test_로그인


settings = get_settings()


@pytest.mark.asyncio
async def test_밴드_생성(client):
    token = await test_로그인(client)
    client.headers.update({"Authorization": f"Bearer {token}"})

    data = {"name": "밴드명"}
    response = await client.post("/api/bands", json=data)
    assert response.status_code == 201
    return response.json()["data"]


@pytest.mark.asyncio
async def test_밴드_조회(client):
    band = await test_밴드_생성(client)

    response = await client.get(f"/api/bands/{band["id"]}")
    assert response.status_code == 200
    return response.json()
