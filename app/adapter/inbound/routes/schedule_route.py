from fastapi import APIRouter, Depends, Path, Query

from app.application.port.input import ScheduleUseCase
from app.application.service.schedule import ScheduleService
from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.http import Http2XX
from app.common.permission import is_authenticated
from app.common.response import APIResponse
from .schemas.base import (
    CreatedResponse,
    PermissionDeniedResponse,
    SuccessResponse,
    UnauthenticatedResponse,
)
from .schemas.schedule import ScheduleInfo, ScheduleResponse

router = APIRouter(prefix="/schedules", tags=["Schedule"])


@router.get(
    "",
    status_code=200,
    summary="일정 리스트 조회",
    responses={
        200: {"description": "일정 조회 성공", "model": SuccessResponse[list[ScheduleResponse]]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def get_schedules(
    band_id: int = Query(title="밴드 PK"),
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: ScheduleUseCase = Depends(ScheduleService),
) -> APIResponse:
    """밴드에 등록된 일정 리스트 조회"""
    schedule = await service.get_band_schedules(credential.user_id, band_id)
    return APIResponse(
        Http2XX.OK,
        data=[ScheduleResponse.from_domain(s).model_dump() for s in schedule],
    )


@router.post(
    "",
    status_code=201,
    summary="일정 등록",
    responses={
        201: {"description": "일정 등록 성공", "model": CreatedResponse[ScheduleResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def create_schedule(
    body: ScheduleInfo,
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: ScheduleUseCase = Depends(ScheduleService),
) -> APIResponse:
    """일정 등록"""
    schedule = await service.create_schedule(
        user_id=credential.user_id, **body.model_dump()
    )
    return APIResponse(Http2XX.CREATED, data=schedule.model_dump())


@router.get(
    "/{band_id}",
    status_code=200,
    summary="일정 정보 조회",
    responses={
        200: {"description": "일정 조회 성공", "model": SuccessResponse[ScheduleResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def get_schedule_info(
    band_id: int = Path(title="밴드 PK"),
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: ScheduleUseCase = Depends(ScheduleService),
) -> APIResponse:
    """일정 정보 조회"""
    schedule = await service.get_schedule_info(band_id)
    return APIResponse(
        Http2XX.OK, data=ScheduleResponse.from_domain(schedule).model_dump()
    )
