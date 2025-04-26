from fastapi import APIRouter, Depends

from app.application.port.input import AuthUseCase
from app.application.service.auth_service import AuthService
from app.common.http import Http2XX
from app.common.response import APIResponse
from .schemas.base import CreatedResponse, SuccessResponse
from .schemas.auth import (
    AutoTokenResponse,
    EmailInfo,
    LoginInfo,
    LoginValidationErrorResponse,
    SignupInfo,
    SignUpValidationErrorResponse,
)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/email/check",
    summary="이메일 중복 체크",
    responses={
        200: {"description": "로그인 성공", "model": SuccessResponse},
        422: {},
    },
)
async def check_email(
    body: EmailInfo, service: AuthUseCase = Depends(AuthService)
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
    body: SignupInfo, service: AuthUseCase = Depends(AuthService)
) -> APIResponse:
    """사용자 정보를 받아 회원가입 후 인증 토큰 반환"""
    return APIResponse(
        Http2XX.CREATED,
        data={"token": await service.signup(**body.model_dump())},
    )


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
    body: LoginInfo, service: AuthUseCase = Depends(AuthService)
) -> APIResponse:
    """사용자 정보를 받아 검증 후 인증 토큰 반환"""
    return APIResponse(
        Http2XX.OK,
        data={"token": await service.login(body.email, body.password)},
    )
