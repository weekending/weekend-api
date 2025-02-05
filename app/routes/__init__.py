from fastapi import APIRouter

from .auth import router as auth_router
from .band import router as band_router
from .document import router as doc_router
from .home import router as home_router
from .schedule import router as schedule_router
from .song import router as song_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(band_router)
router.include_router(doc_router)
# router.include_router(home_router)
router.include_router(schedule_router)
router.include_router(song_router)


@router.get("/", include_in_schema=False)
def healthcheck() -> str:
    return "ok"
