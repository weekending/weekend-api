from fastapi import APIRouter, Depends

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.http import Http2XX
from app.common.permission import is_authenticated
from app.common.response import APIResponse
from app.schemas.base import (
    PermissionDeniedResponse,
    SuccessResponse,
    UnauthenticatedResponse,
)
from app.schemas.user import UserBandResponse, UserInfoResponse
from app.service.band import BandService
from app.service.user import UserService

router = APIRouter(prefix="/api/users", tags=["User"])


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
    service: UserService = Depends(UserService),
) -> APIResponse:
    """사용자 정보 조회"""
    return APIResponse(
        Http2XX.OK, data=await service.get_user_info(credential.user_id)
    )


@router.get(
    "/me/bands",
    summary="사용자 밴드 조회",
    responses={
        200: {"description": "조회 성공", "model": SuccessResponse[list[UserBandResponse]]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def get_user_bands(
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: BandService = Depends(BandService),
) -> APIResponse:
    """사용자가 가입한 밴드 리스트 조회"""
    return APIResponse(
        Http2XX.OK,
        data=await service.get_user_bands(credential.user_id),
    )
