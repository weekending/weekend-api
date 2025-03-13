from bcrypt import checkpw, gensalt, hashpw
from fastapi import Depends

from app.adapter.outbound.persistence import UserPersistenceAdapter
from app.common.auth.jwt_provider import JWTProvider
from app.common.exception import APIException
from app.common.http import Http4XX
from app.domain import User
from ..port.input import AuthUseCase
from ..port.output import UserRepositoryPort


class AuthService(AuthUseCase):
    def __init__(
        self,
        jwt: JWTProvider = Depends(JWTProvider),
        user_repo: UserRepositoryPort = Depends(UserPersistenceAdapter),
    ):
        self._jwt = jwt
        self._user_repo = user_repo

    async def check_email_exists(self, email: str) -> bool:
        if await self._user_repo.find_by_email(email):
            raise APIException(Http4XX.DUPLICATED_EMAIL)
        return True

    async def signup(
        self, name: str, email: str, password: str, password_check: str
    ) -> str:
        if password != password_check:
            raise APIException(Http4XX.PASSWORD_MISMATCHED)
        elif await self._user_repo.find_by_email(email):
            raise APIException(Http4XX.DUPLICATED_EMAIL)
        user = await self._user_repo.save(
            User(
                name=name,
                email=email,
                password=hashpw(password.encode(), salt=gensalt()).decode(),
                is_active=True,
                is_admin=False,
            )
        )
        return self._jwt.encode_token(user)

    async def login(self, email: str, password: str) -> str:
        if not (user := await self._user_repo.find_by_email(email)):
            raise APIException(Http4XX.AUTHENTICATION_FAILED, detail="가입하지 않은 회원.")
        elif not checkpw(password.encode(), user.password.encode()):
            raise APIException(Http4XX.AUTHENTICATION_FAILED, detail="비밀번호 불일치")
        return self._jwt.encode_token(user)
