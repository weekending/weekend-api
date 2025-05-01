from unittest.mock import Mock

import pytest

from app.application.service.auth_service import AuthService
from app.common.exception import APIException
from app.common.http import Http4XX
from .factory import UserFactory


@pytest.mark.asyncio
async def test_유효한_이메일(user_repo):
    mock_jwt = Mock()
    user_repo.find_by_email.return_value = None

    service = AuthService(mock_jwt, user_repo)
    result = await service.check_email_exists("test@test.com")
    assert result is True


@pytest.mark.asyncio
async def test_중복된_이메일_에러(user_repo):
    mock_jwt = Mock()
    user_repo.find_by_email.return_value = UserFactory.generate()

    service = AuthService(mock_jwt, user_repo)
    with pytest.raises(APIException) as exc:
        await service.check_email_exists("test@test.com")
    assert exc.value.http == Http4XX.DUPLICATED_EMAIL


@pytest.mark.asyncio
async def test_회원가입_및_토큰_생성(user_repo):
    new_user = UserFactory.generate()
    mock_jwt = Mock()
    mock_jwt.encode_token.return_value = "auth-token"
    user_repo.find_by_email.return_value = None
    user_repo.save.return_value = new_user

    service = AuthService(mock_jwt, user_repo)
    token = await service.signup("test", "test@test.com", "password", "password")

    assert token == "auth-token"
    user_repo.save.assert_called_once()
    mock_jwt.encode_token.assert_called_once_with(new_user)


@pytest.mark.asyncio
async def test_회원가입_비밀번호_불일치_에러(user_repo):
    mock_jwt = Mock()
    user_repo.find_by_email.return_value = None

    service = AuthService(mock_jwt, user_repo)
    with pytest.raises(APIException) as exc:
        await service.signup("test", "test@test.com", "password", "pass")
    assert exc.value.http == Http4XX.PASSWORD_MISMATCHED


@pytest.mark.asyncio
async def test_이미_가입한_이메일_에러(user_repo):
    mock_jwt = Mock()
    user_repo.find_by_email.return_value = UserFactory.generate()

    service = AuthService(mock_jwt, user_repo)
    with pytest.raises(APIException) as exc:
        await service.signup("test", "test@test.com", "password", "password")
    assert exc.value.http == Http4XX.DUPLICATED_EMAIL


@pytest.mark.asyncio
async def test_존재하지_않는_이메일로_로그인(user_repo):
    mock_jwt = Mock()
    user_repo.find_by_email.return_value = None

    service = AuthService(mock_jwt, user_repo)
    with pytest.raises(APIException) as exc:
        await service.login("test@test.com", "password")
    assert exc.value.http == Http4XX.AUTHENTICATION_FAILED


@pytest.mark.asyncio
async def test_로그인_및_토큰_생성(user_repo):
    password = "qwe123!"
    user = UserFactory.generate(password=password)
    mock_jwt = Mock()
    mock_jwt.encode_token.return_value = "auth-token"
    user_repo.find_by_email.return_value = user

    service = AuthService(mock_jwt, user_repo)
    token = await service.login("test@test.com", password)

    assert token == "auth-token"
    mock_jwt.encode_token.assert_called_once_with(user)


@pytest.mark.asyncio
async def test_잘못된_비밀번호로_로그인(user_repo):
    mock_jwt = Mock()
    user_repo.find_by_email.return_value = UserFactory.generate(password="123")

    service = AuthService(mock_jwt, user_repo)
    with pytest.raises(APIException) as exc:
        await service.login("test@test.com", "password")
    assert exc.value.http == Http4XX.AUTHENTICATION_FAILED
