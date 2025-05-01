import pytest


@pytest.mark.asyncio
async def test_메인_화면(client):
    response = await client.get("")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_로그인_화면(client):
    response = await client.get("/login")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_회원가입_화면(client):
    response = await client.get("/signup")
    assert response.status_code == 200
