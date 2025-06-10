from fastapi import APIRouter, Depends, Path, Query

from app.application.port.input import PostUseCase
from app.application.service.post_service import PostService
from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.http import Http2XX
from app.common.permission import allow_any
from app.common.response import APIResponse
from .schemas.base import (
    CreatedResponse,
    PermissionDeniedResponse,
    SuccessResponse,
    UnauthenticatedResponse,
)
from .schemas.post import (
    PostCreateInfo,
    PostResponse,
    PostUpdateInfo,
    PostListResponse,
)

router = APIRouter(prefix="/posts", tags=["Post"])


@router.get(
    "",
    status_code=200,
    summary="게시물 리스트 조회",
    responses={
        200: {
            "description": "게시물 조회 성공",
            "model": SuccessResponse[list[PostListResponse]],
        },
        422: {},
    },
)
async def get_posts(
    category_id: int = Query(title="카테고리 PK"),
    page: int = Query(title="페이지 번호", default=1),
    size: int = Query(title="페이지네이션 사이즈", default=15),
    service: PostUseCase = Depends(PostService),
) -> APIResponse:
    """특정 카테고리의 게시물 리스트 조회"""
    posts = await service.get_post_list(size, page, category_id)
    return APIResponse(
        Http2XX.OK, data=[PostListResponse.from_domain(post) for post in posts]
    )


@router.get(
    "/count",
    status_code=200,
    summary="게시물 개수",
    responses={
        200: {"description": "조회 성공", "model": SuccessResponse},
        422: {},
    },
)
async def get_post_count(
    category_id: int = Query(title="카테고리 PK", default=0),
    service: PostUseCase = Depends(PostService),
) -> APIResponse:
    """게시물 개수 조회"""
    count = await service.get_post_count(category_id)
    return APIResponse(Http2XX.OK, data={"count": count})


@router.post(
    "",
    status_code=201,
    summary="게시물 등록",
    responses={
        201: {"description": "등록 성공", "model": CreatedResponse[PostResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def create_post(
    body: PostCreateInfo,
    credential: JWTAuthorizationCredentials = Depends(allow_any),
    service: PostUseCase = Depends(PostService),
) -> APIResponse:
    """게시물 등록"""
    post = await service.create_post(
        user_id=credential.user_id, **body.model_dump()
    )
    return APIResponse(Http2XX.CREATED, data=post)


@router.get(
    "/{post_id}",
    status_code=200,
    summary="게시물 정보 조회",
    responses={
        200: {"description": "조회 성공", "model": SuccessResponse[PostResponse]},
        422: {},
    },
)
async def get_post_info(
    post_id: int = Path(title="게시물 PK"),
    service: PostUseCase = Depends(PostService),
) -> APIResponse:
    """게시물 정보 조회"""
    post = await service.get_post_info(post_id)
    return APIResponse(Http2XX.OK, data=PostResponse.from_domain(post))


@router.patch(
    "/{post_id}",
    status_code=200,
    summary="게시물 수정",
    responses={
        200: {"description": "수정 성공", "model": SuccessResponse[PostResponse]},
        401: UnauthenticatedResponse.to_openapi(),
        403: PermissionDeniedResponse.to_openapi(),
        422: {},
    },
)
async def update_post(
    body: PostUpdateInfo,
    post_id: int = Path(title="게시물 PK"),
    credential: JWTAuthorizationCredentials = Depends(allow_any),
    service: PostUseCase = Depends(PostService),
) -> APIResponse:
    """게시물 수정"""
    post = await service.update_post(
        post_id, user_id=credential.user_id, **body.model_dump()
    )
    return APIResponse(Http2XX.OK, data=PostResponse.from_domain(post))
