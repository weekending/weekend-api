from fastapi import Depends

from app.common.auth.jwt_provider import JWTProvider
from app.common.exception import APIException
from app.common.http import Http4XX
from app.models import User
from app.schemas.auth import LoginInfo, SignupInfo


class AuthService:
    def __init__(self, jwt: JWTProvider = Depends(JWTProvider)):
        self.jwt = jwt

    async def check_email_exists(self, email: str) -> bool:
        if await User.find_one(User.email == email):
            raise APIException(Http4XX.DUPLICATED_EMAIL)
        return True

    async def signup(self, data: SignupInfo) -> str:
        if await User.find_one(User.email == data.email):
            raise APIException(Http4XX.DUPLICATED_EMAIL)
        elif data.password != data.password_check:
            raise APIException(Http4XX.PASSWORD_MISMATCHED)
        user = User(**data.model_dump(exclude={"password_check"}))
        await user.save()
        return self.jwt.encode_token(user)

    async def login(self, data: LoginInfo) -> str:
        if not (user := await User.find_one(User.email == data.email)):
            raise APIException(Http4XX.AUTHENTICATION_FAILED, detail="가입하지 않은 회원.")
        elif not user.check_password(data.password):
            raise APIException(Http4XX.AUTHENTICATION_FAILED, detail="비밀번호 불일치")
        return self.jwt.encode_token(user)
