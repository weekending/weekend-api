from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.permission import is_authenticated
from app.schemas.band import BandInfo
from app.service.band import BandService

router = APIRouter(prefix="/api/band")


@router.post("")
async def create_band(
    body: BandInfo,
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: BandService = Depends(BandService),
) -> JSONResponse:
    """밴드 생성"""
    return JSONResponse(
        content=await service.create_band(body, credential.user_id),
        status_code=201,
    )


@router.get("/{band_id}")
async def get_band_info(
    band_id: int,
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: BandService = Depends(BandService),
) -> JSONResponse:
    """밴드 정보 조회"""
    return JSONResponse(
        content=await service.get_band_info(band_id), status_code=200
    )
