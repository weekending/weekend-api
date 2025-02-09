from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.permission import is_authenticated
from app.schemas.base import PermissionDeniedResponse, UnauthenticatedResponse
from app.schemas.user import UserBandResponse, UserInfoResponse
from app.service.band import BandService
from app.service.user import UserService

router = APIRouter(prefix="/api/users", tags=["User"])


@router.get(
    "/me/info",
    summary="사용자 정보 조회",
    responses={
        200: {"description": "조회 성공", "model": UserInfoResponse},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def get_user_bands(
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: UserService = Depends(UserService),
) -> JSONResponse:
    """사용자 정보 조회"""
    return JSONResponse(
        content=await service.get_user_info(credential.user_id)
    )


@router.get(
    "/me/bands",
    summary="사용자 밴드 조회",
    responses={
        200: {"description": "조회 성공", "model": list[UserBandResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def get_user_bands(
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: BandService = Depends(BandService),
) -> JSONResponse:
    """사용자가 가입한 밴드 리스트 조회"""
    return JSONResponse(
        content=await service.get_user_bands(credential.user_id),
    )
