from pydantic import BaseModel, Field

from .base import BaseErrorResponse


class SignupInfo(BaseModel):
    name: str = Field(title="닉네임", examples=["미민또"])
    email: str = Field(title="이메일", examples=["weekend.dev@gmail.com"])
    password: str = Field(title="비밀번호", examples=["1q2w3e4r!"])
    password_check: str = Field(title="비밀번호 확인", examples=["1q2w3e4r!"])


class LoginInfo(BaseModel):
    email: str = Field(title="이메일", examples=["weekend.dev@gmail.com"])
    password: str = Field(title="비밀번호", examples=["1q2w3e4r!"])


class AutoTokenResponse(BaseModel):
    token: str = Field(title="인증 토큰", examples=["eyJhbGciOiJIUzI1NiIs..."])


class SignUpValidationErrorResponse(BaseErrorResponse):
    """파라미터 에러"""

    response_extra = {
        "examples": {
            "비밀번호가 다른 경우": {
                "value": {"detail": "같은 비밀번호를 입력해주세요."}
            },
            "아이디가 중복된 경우": {
                "value": {"detail": "중복된 이메일입니다."}
            }
        }
    }


class LoginValidationErrorResponse(BaseErrorResponse):
    """파라미터 에러"""

    response_extra = {
        "examples": {
            "이메일이 없는 경우": {
                "value": {"detail": "가입하지 않은 회원입니다."}
            },
            "비밀번호를 틀린 경우": {
                "value": {"detail": "비밀번호가 일치하지 않습니다."}
            }
        }
    }
