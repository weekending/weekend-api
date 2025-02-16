from fastapi import APIRouter, Depends, Path

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.http import Http2XX
from app.common.permission import is_authenticated
from app.common.response import APIResponse
from app.schemas.band import BandInfo, BandNotFoundResponse, BandResponse
from app.schemas.base import (
    CreatedResponse,
    PermissionDeniedResponse,
    SuccessResponse,
    UnauthenticatedResponse,
)
from app.service.band import BandService

router = APIRouter(prefix="/api/band", tags=["Band"])


@router.post(
    "",
    status_code=201,
    summary="밴드 생성",
    responses={
        201: {"description": "밴드 생성 성공", "model": CreatedResponse[BandResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def create_band(
    body: BandInfo,
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: BandService = Depends(BandService),
) -> APIResponse:
    """입력받은 이름의 밴드 생성"""
    return APIResponse(
        Http2XX.CREATED,
        data=await service.create_band(body, credential.user_id),
    )


@router.get(
    "/{band_id}",
    summary="밴드 정보 조회",
    responses={
        200: {"description": "밴드 조회 성공", "model": SuccessResponse[BandResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        404: BandNotFoundResponse.to_openapi(),
        422: {},
    },
)
async def get_band_info(
    band_id: int = Path(title="밴드 PK"),
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: BandService = Depends(BandService),
) -> APIResponse:
    """밴드 정보 조회"""
    return APIResponse(Http2XX.OK, data=await service.get_band_info(band_id))
