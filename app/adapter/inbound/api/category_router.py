from fastapi import APIRouter, Depends

from app.application.port.input import PostCategoryUseCase
from app.application.service.category_service import PostCategoryService
from app.common.http import Http2XX
from app.common.response import APIResponse
from .schemas.base import (
    PermissionDeniedResponse,
    SuccessResponse,
    UnauthenticatedResponse,
)
from .schemas.category import CategoryResponse

router = APIRouter(prefix="/categories", tags=["Category"])


@router.get(
    "",
    status_code=200,
    summary="카테고리 리스트 조회",
    responses={
        200: {
            "description": "조회 성공",
            "model": SuccessResponse[list[CategoryResponse]]
        },
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def get_categories(
    service: PostCategoryUseCase = Depends(PostCategoryService),
) -> APIResponse:
    """카테고리 리스트 조회"""
    categories = await service.get_active_categories()
    return APIResponse(
        Http2XX.OK,
        data=[CategoryResponse.from_domain(cat) for cat in categories],
    )
