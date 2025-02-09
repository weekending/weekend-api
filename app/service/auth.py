from fastapi import Depends
from starlette.exceptions import HTTPException

from app.common.auth.jwt_provider import JWTProvider
from app.models import User
from app.schemas.auth import LoginInfo, SignupInfo


class AuthService:
    def __init__(self, jwt: JWTProvider = Depends(JWTProvider)):
        self.jwt = jwt

    async def signup(self, data: SignupInfo) -> str:
        if await User.find_one(User.email == data.email):
            raise HTTPException(status_code=400, detail="중복된 이메일입니다.")
        elif data.password != data.password_check:
            raise HTTPException(status_code=400, detail="같은 비밀번호를 입력해주세요.")
        user = User(**data.model_dump(exclude={"password_check"}))
        await user.save()
        return self.jwt.encode_token(user)

    async def login(self, data: LoginInfo) -> str:
        if not (user := await User.find_one(User.email == data.email)):
            raise HTTPException(status_code=400, detail="가입하지 않은 회원입니다.")
        elif not user.check_password(data.password):
            raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")
        return self.jwt.encode_token(user)
