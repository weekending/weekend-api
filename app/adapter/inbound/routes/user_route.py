from fastapi import APIRouter, Depends

from app.application.port.input import UserUseCase
from app.application.service.user import UserService
from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.http import Http2XX
from app.common.permission import is_authenticated
from app.common.response import APIResponse
from .schemas.band import BandResponse
from .schemas.base import (
    PermissionDeniedResponse,
    SuccessResponse,
    UnauthenticatedResponse,
)
from .schemas.user import UserInfoResponse

router = APIRouter(prefix="/users", tags=["User"])


@router.get(
    "/me/info",
    summary="사용자 정보 조회",
    responses={
        200: {"description": "조회 성공", "model": SuccessResponse[UserInfoResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def get_user_bands(
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: UserUseCase = Depends(UserService),
) -> APIResponse:
    """사용자 정보 조회"""
    user = await service.get_user_info(credential.user_id)
    return APIResponse(
        Http2XX.OK, data=UserInfoResponse.from_domain(user).model_dump()
    )


@router.get(
    "/me/bands",
    summary="사용자 밴드 조회",
    responses={
        200: {"description": "조회 성공", "model": SuccessResponse[list[BandResponse]]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def get_user_bands(
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: UserUseCase = Depends(UserService),
) -> APIResponse:
    """사용자가 가입한 밴드 리스트 조회"""
    bands = await service.get_user_bands(credential.user_id)
    return APIResponse(Http2XX.OK, data=[band.model_dump() for band in bands])
