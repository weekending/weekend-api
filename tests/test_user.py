import pytest

from .test_band import test_밴드_생성


@pytest.mark.asyncio
async def test_사용자_밴드_조회(client):
    await test_밴드_생성(client)

    response = await client.get("/api/users/me/bands")
    assert response.status_code == 200
    band = response.json()
    assert len(band["data"]) == 1
