from fastapi import APIRouter, Depends, Path, Query

from app.application.port.input import NoticeUseCase
from app.application.service.notice_service import NoticeService
from app.common.http import Http2XX
from app.common.response import APIResponse
from .schemas.base import SuccessResponse
from .schemas.notice import NoticeResponse

router = APIRouter(prefix="/notice", tags=["Notice"])


@router.get(
    "",
    status_code=200,
    summary="공지 리스트 조회",
    responses={
        200: {
            "description": "공지 조회 성공",
            "model": SuccessResponse[list[NoticeResponse]],
        },
        422: {},
    },
)
async def get_notice_list(
    page: int = Query(title="페이지 번호", default=1),
    size: int = Query(title="페이지네이션 사이즈", default=10),
    service: NoticeUseCase = Depends(NoticeService),
) -> APIResponse:
    """공지 리스트 조회"""
    notices = await service.get_notice_list(size, page)
    return APIResponse(
        Http2XX.OK, data=[NoticeResponse.from_domain(notice) for notice in notices]
    )


@router.get(
    "/{notice_id}",
    status_code=200,
    summary="공지 정보 조회",
    responses={
        200: {"description": "조회 성공", "model": SuccessResponse[NoticeResponse]},
        422: {},
    },
)
async def get_notice_info(
    notice_id: int = Path(title="공지 PK"),
    service: NoticeUseCase = Depends(NoticeService),
) -> APIResponse:
    """공지 정보 조회"""
    notice = await service.get_notice_info(notice_id)
    return APIResponse(Http2XX.OK, data=NoticeResponse.from_domain(notice))
