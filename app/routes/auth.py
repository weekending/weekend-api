from fastapi import APIRouter, Depends

from app.common.http import Http2XX
from app.common.response import APIResponse
from app.schemas.base import CreatedResponse, SuccessResponse
from app.schemas.auth import (
    AutoTokenResponse,
    EmailInfo,
    LoginInfo,
    LoginValidationErrorResponse,
    SignupInfo,
    SignUpValidationErrorResponse,
)
from app.service.auth import AuthService

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post(
    "/email/check",
    summary="이메일 중복 체크",
    responses={
        200: {"description": "로그인 성공", "model": SuccessResponse},
        422: {},
    },
)
async def check_email(
    body: EmailInfo,
    service: AuthService = Depends(AuthService)
) -> APIResponse:
    return APIResponse(
        Http2XX.OK, data=await service.check_email_exists(body.email)
    )


@router.post(
    "/signup",
    status_code=201,
    summary="회원가입",
    responses={
        201: {"description": "회원가입 성공", "model": CreatedResponse[AutoTokenResponse]},
        400: SignUpValidationErrorResponse.to_openapi(),
        422: {},
    },
)
async def signup(
    body: SignupInfo, service: AuthService = Depends(AuthService)
) -> APIResponse:
    """사용자 정보를 받아 회원가입 후 인증 토큰 반환"""
    return APIResponse(Http2XX.CREATED, data={"token": await service.signup(body)})


@router.post(
    "/login",
    summary="로그인",
    responses={
        200: {"description": "로그인 성공", "model": CreatedResponse[AutoTokenResponse]},
        400: LoginValidationErrorResponse.to_openapi(),
        422: {},
    },
)
async def login(
    body: LoginInfo, service: AuthService = Depends(AuthService)
) -> APIResponse:
    """사용자 정보를 받아 검증 후 인증 토큰 반환"""
    return APIResponse(Http2XX.OK, data={"token": await service.login(body)})
