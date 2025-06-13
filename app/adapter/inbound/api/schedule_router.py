from datetime import date

from fastapi import APIRouter, Depends, Path, Query

from app.application.port.input import ScheduleUseCase
from app.application.service.schedule_service import ScheduleService
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
from .schemas.schedule import (
    ScheduleInfo,
    ScheduleResponse,
    ScheduleUpdateInfo,
)

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
    from_: date = Query(title="조회 시작일", default=None, alias="from"),
    to: date = Query(title="조회 종료일", default=None),
    # credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: ScheduleUseCase = Depends(ScheduleService),
) -> APIResponse:
    """밴드에 등록된 일정 리스트 조회"""
    schedule = await service.get_band_schedules(-1, band_id, from_, to)
    return APIResponse(
        Http2XX.OK, data=[ScheduleResponse.from_domain(s) for s in schedule]
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
    return APIResponse(Http2XX.CREATED, data=schedule)


@router.get(
    "/{schedule_id}",
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
    schedule_id: int = Path(title="스케줄 PK"),
    # credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: ScheduleUseCase = Depends(ScheduleService),
) -> APIResponse:
    """일정 정보 조회"""
    schedule = await service.get_schedule_info(schedule_id)
    return APIResponse(
        Http2XX.OK, data=ScheduleResponse.from_domain(schedule)
    )


@router.patch(
    "/{schedule_id}",
    status_code=200,
    summary="일정 정보 변경",
    responses={
        200: {"description": "일정 정보 변경 성공", "model": SuccessResponse[ScheduleResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def update_schedule(
    body: ScheduleUpdateInfo,
    schedule_id: int = Path(title="스케줄 PK"),
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: ScheduleUseCase = Depends(ScheduleService),
) -> APIResponse:
    """일정 정보 변경"""
    schedule = await service.update_schedule_info(
        schedule_id, credential.user_id, **body.model_dump()
    )
    return APIResponse(
        Http2XX.OK, data=ScheduleResponse.from_domain(schedule)
    )


@router.post(
    "/{schedule_id}/attend",
    status_code=200,
    summary="일정 참여",
    responses={
        200: {"description": "일정 참여 성공", "model": SuccessResponse[ScheduleResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def attend_schedule(
    schedule_id: int = Path(title="스케줄 PK"),
    credential: JWTAuthorizationCredentials = Depends(is_authenticated),
    service: ScheduleUseCase = Depends(ScheduleService),
) -> APIResponse:
    """일정 참여"""
    return APIResponse(
        Http2XX.OK,
        data=await service.attend_schedule(schedule_id, credential.user_id),
    )
