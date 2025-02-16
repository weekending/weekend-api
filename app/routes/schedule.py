from fastapi import APIRouter, Depends

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.http import Http2XX
from app.common.permission import is_authenticated
from app.common.response import APIResponse
from app.schemas.base import (
    CreatedResponse,
    PermissionDeniedResponse,
    UnauthenticatedResponse,
)
from app.schemas.schedule import ScheduleInfo
from app.service.schedule import ScheduleService

router = APIRouter(prefix="/api/schedule", tags=["Schedule"])


@router.post(
    "",
    status_code=201,
    summary="일정 등록",
    responses={
        201: {"description": "일정 등록 성공", "model": CreatedResponse},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def create_schedule(
    body: ScheduleInfo,
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: ScheduleService = Depends(ScheduleService),
) -> APIResponse:
    """일정 등록"""
    return APIResponse(
        Http2XX.CREATED,
        data=await service.create_schedule(body, credential.user_id),
    )
