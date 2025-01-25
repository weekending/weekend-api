from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.permission import leader_only
from app.schemas.schedule import ScheduleInfo
from app.service.schedule import ScheduleService

router = APIRouter(prefix="/api/schedule")


@router.post("")
async def create_schedule(
    body: ScheduleInfo,
    credential: JWTAuthorizationCredentials = Depends(leader_only),
    service: ScheduleService = Depends(ScheduleService),
) -> JSONResponse:
    """일정 등록"""
    return JSONResponse(
        content=await service.create_schedule(body, credential.user_id),
        status_code=201,
    )
