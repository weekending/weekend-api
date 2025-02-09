from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.permission import is_authenticated
from app.schemas.base import PermissionDeniedResponse, UnauthenticatedResponse
from app.schemas.schedule import ScheduleInfo
from app.service.schedule import ScheduleService

router = APIRouter(prefix="/api/schedule", tags=["Schedule"])


@router.post(
    "",
    status_code=201,
    summary="일정 등록",
    responses={
        201: {"description": "일정 등록 성공"},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def create_schedule(
    body: ScheduleInfo,
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: ScheduleService = Depends(ScheduleService),
) -> JSONResponse:
    """일정 등록"""
    return JSONResponse(
        content=await service.create_schedule(body, credential.user_id),
        status_code=201,
    )
