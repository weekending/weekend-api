from datetime import datetime

from fastapi import APIRouter, Depends, Request

from app.application.port.input import ScheduleUseCase
from app.application.service.schedule_service import ScheduleService
from app.common.auth.authentication import JWTAuthorizationCredentials
from app.common.permission import cookie_allow_any, cookie_authenticated
from app.common.template import template
from app.common.utils import format_time, to_weekday, localtime

router = APIRouter(prefix="/schedules")


@router.get("")
async def schedule_list(request: Request):
    """일정 리스트"""
    return template.TemplateResponse(request, "/schedule/schedule.html")


@router.get("/register")
async def register_schedule(
    request: Request,
    credential: JWTAuthorizationCredentials = Depends(cookie_authenticated),
):
    """일정 등록"""
    return template.TemplateResponse(
        request,
        "/schedule/schedule-detail.html",
        context={"nav_title": "일정 등록", "is_register": True, "is_edit": False},
    )


@router.get("/{schedule_id}")
async def schedule_detail(
    schedule_id: int,
    request: Request,
    credential: JWTAuthorizationCredentials = Depends(cookie_allow_any),
    now: datetime = Depends(localtime),
    service: ScheduleUseCase = Depends(ScheduleService),
):
    """일정 상세"""
    schedule = await service.get_schedule_info(schedule_id)
    return template.TemplateResponse(
        request,
        "/schedule/schedule-detail.html",
        context={
            "title": schedule.title,
            "date": f'{schedule.day.strftime("%Y.%m.%d")} ({to_weekday(schedule.day)})',
            "time": f'{format_time(schedule.start_time)} ~ {format_time(schedule.end_time)}',
            "location": schedule.location,
            "user_count": len(schedule.users),
            "usernames": ", ".join([u.name for u in schedule.users]),
            "memo": schedule.memo or "",
            "is_register": False,
            "is_edit": False,
            "is_attended": credential.user_id in [u.id for u in schedule.users],
            "can_attend": schedule.day >= now.date(),
        },
    )


@router.get("/{schedule_id}/edit")
async def edit_schedule(
    schedule_id: int,
    request: Request,
    credential: JWTAuthorizationCredentials = Depends(cookie_authenticated),
    service: ScheduleUseCase = Depends(ScheduleService),
):
    """일정 수정"""
    schedule = await service.get_schedule_info(schedule_id)
    return template.TemplateResponse(
        request,
        "/schedule/schedule-detail.html",
        context={
            "nav_title": "일정 수정",
            "title": schedule.title,
            "date": schedule.day.strftime("%Y-%m-%d"),
            "start_time": schedule.start_time,
            "end_time": schedule.end_time,
            "location": schedule.location,
            "user_count": len(schedule.users),
            "usernames": ", ".join([u.name for u in schedule.users]),
            "memo": schedule.memo or "",
            "is_register": False,
            "is_edit": True,
        },
    )
