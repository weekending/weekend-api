from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.models import PermissionType
from app.schemas.auth import (
    AutoTokenResponse,
    LoginInfo,
    LoginValidationErrorResponse,
    SignupInfo,
    SignUpValidationErrorResponse,
)
from app.service.auth import AuthService

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post(
    "/signup",
    status_code=201,
    summary="회원가입",
    responses={
        201: {"description": "회원가입 성공", "model": AutoTokenResponse},
        400: SignUpValidationErrorResponse.to_openapi(),
        422: {},
    },
)
async def signup(
    body: SignupInfo, service: AuthService = Depends(AuthService)
) -> JSONResponse:
    """사용자 정보를 받아 회원가입 후 인증 토큰 반환"""
    token = await service.signup(body, permission=PermissionType.LEADER)
    return JSONResponse(content={"token": token}, status_code=201)


@router.post(
    "/login",
    summary="로그인",
    responses={
        200: {"description": "로그인 성공", "model": AutoTokenResponse},
        400: LoginValidationErrorResponse.to_openapi(),
        422: {},
    },
)
async def login(
    body: LoginInfo, service: AuthService = Depends(AuthService)
) -> JSONResponse:
    """사용자 정보를 받아 검증 후 인증 토큰 반환"""
    return JSONResponse(content={"token": await service.login(body)})
