import pytest

from app.core.settings import get_settings


settings = get_settings()

NAME = "테스트사용자"
USERNAME = "test_user"
PASSWORD = "test-password"


@pytest.mark.asyncio
async def test_회원가입(client):
    data = {
        "name": NAME,
        "username": USERNAME,
        "password": PASSWORD,
        "password_check": PASSWORD,
    }
    response = await client.post("/api/auth/signup", json=data)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_일치하지않는_비밀번호로_회원가입(client):
    data = {
        "name": NAME,
        "username": USERNAME,
        "password": PASSWORD,
        "password_check": PASSWORD + "123",
    }
    response = await client.post("/api/auth/signup", json=data)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_중복된_이메일로_회원가입(client):
    await test_회원가입(client)

    data = {
        "name": NAME,
        "username": USERNAME,
        "password": PASSWORD,
        "password_check": PASSWORD,
    }
    response = await client.post("/api/auth/signup", json=data)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_로그인(client):
    await test_회원가입(client)

    data = {
        "username": USERNAME,
        "password": PASSWORD,
    }
    response = await client.post("/api/auth/login", json=data)
    assert response.status_code == 200
    res_json = response.json()
    return res_json["token"]


@pytest.mark.asyncio
async def test_잘못된_이메일로_로그인(client):
    await test_회원가입(client)

    data = {
        "username": USERNAME + "123",
        "password": PASSWORD,
    }
    response = await client.post("/api/auth/login", json=data)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_잘못된_비밀번호로_로그인(client):
    await test_회원가입(client)

    data = {
        "username": USERNAME,
        "password": PASSWORD + "123",
    }
    response = await client.post("/api/auth/login", json=data)
    assert response.status_code == 400
