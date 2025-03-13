from fastapi import APIRouter

from .auth_route import router as auth_router
from .band_route import router as band_router
from .document_route import router as doc_router
from .schedule_route import router as schedule_router
from .song_route import router as song_router
from .user_route import router as user_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(band_router)
router.include_router(doc_router)
# router.include_router(home_router)
router.include_router(schedule_router)
router.include_router(song_router)
router.include_router(user_router)


@router.get("/", include_in_schema=False)
def healthcheck() -> str:
    return "ok"
