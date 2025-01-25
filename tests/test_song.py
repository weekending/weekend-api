import pytest

from app.core.settings import get_settings
from .test_band import test_밴드_생성


settings = get_settings()


@pytest.mark.asyncio
async def test_곡_등록(client):
    await test_밴드_생성(client)

    data = {
        "title": "밤편지",
        "singer": "야이유",
    }
    response = await client.post("/api/songs", json=data)
    assert response.status_code == 201
