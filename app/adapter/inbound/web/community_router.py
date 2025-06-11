from fastapi import APIRouter, Depends, Request

from app.application.port.input import PostCategoryUseCase, PostUseCase
from app.application.service.category_service import PostCategoryService
from app.application.service.post_service import PostService
from app.common.auth.schemas import JWTAuthorizationCredentials
from app.common.permission import cookie_allow_any
from app.common.template import template

router = APIRouter()


@router.get("/community")
async def community(
    request: Request,
    category_id: int = 0,
    page: int = 1,
    service: PostCategoryUseCase = Depends(PostCategoryService),
):
    """게시물 화면"""
    categories = await service.get_active_categories()
    return template.TemplateResponse(
        request,
        "/post/post.html",
        context={
            "categories": categories,
            "category_id": category_id,
            "page": page,
        },
    )


@router.get("/community/posts/{post_id}")
async def community_post_detail(
    request: Request,
    post_id: int,
    credential: JWTAuthorizationCredentials = Depends(cookie_allow_any),
    service: PostUseCase = Depends(PostService),
):
    """게시물 상세 화면"""
    post = await service.get_post_info(post_id)
    return template.TemplateResponse(
        request,
        "/post/post-detail.html",
        context={"post": post, "is_owner": post.user_id == credential.user_id},
    )
