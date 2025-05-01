import pytest

from app.core.settings import get_settings


settings = get_settings()

NAME = "테스트사용자"
EMAIL = "test_user"
PASSWORD = "test-password"


@pytest.mark.asyncio
async def test_이메일_중복여부_확인(client):
    data = {"email": EMAIL}
    response = await client.post("/api/auth/email/check", json=data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_회원가입후_이메일_중복여부_확인(client):
    await test_회원가입(client)

    data = {"email": EMAIL}
    response = await client.post("/api/auth/email/check", json=data)
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_회원가입(client):
    data = {
        "name": NAME,
        "email": EMAIL,
        "password": PASSWORD,
        "password_check": PASSWORD,
    }
    response = await client.post("/api/auth/signup", json=data)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_일치하지않는_비밀번호로_회원가입(client):
    data = {
        "name": NAME,
        "email": EMAIL,
        "password": PASSWORD,
        "password_check": PASSWORD + "123",
    }
    response = await client.post("/api/auth/signup", json=data)
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_중복된_이메일로_회원가입(client):
    await test_회원가입(client)

    data = {
        "name": NAME,
        "email": EMAIL,
        "password": PASSWORD,
        "password_check": PASSWORD,
    }
    response = await client.post("/api/auth/signup", json=data)
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_로그인(client):
    await test_회원가입(client)

    data = {
        "email": EMAIL,
        "password": PASSWORD,
    }
    response = await client.post("/api/auth/login", json=data)
    assert response.status_code == 200
    res_json = response.json()
    return res_json["data"]["token"]


@pytest.mark.asyncio
async def test_잘못된_이메일로_로그인(client):
    await test_회원가입(client)

    data = {
        "email": EMAIL + "123",
        "password": PASSWORD,
    }
    response = await client.post("/api/auth/login", json=data)
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_잘못된_비밀번호로_로그인(client):
    await test_회원가입(client)

    data = {
        "email": EMAIL,
        "password": PASSWORD + "123",
    }
    response = await client.post("/api/auth/login", json=data)
    assert response.status_code == 422
