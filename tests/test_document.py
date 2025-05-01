from unittest.mock import Mock, patch

import pytest

from app.domain import User
from .test_auth import test_로그인


@pytest.mark.asyncio
async def test_문서_조회시_로그인_페이지_이동(client):
    response = await client.get("/docs")
    assert response.status_code == 302


@pytest.mark.asyncio
async def test_문서_로그인_페이지(client):
    response = await client.get("/docs/login")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_문서_조회(client):
    token = await test_로그인(client)
    with patch(
        "app.application.service.user_service.UserService.get_user_info"
    ) as mock_get_user_info:
        mock_get_user_info.return_value = Mock(User, is_admin=True)
        response = await client.get("/docs", cookies={"token": token})
    assert response.status_code == 200
