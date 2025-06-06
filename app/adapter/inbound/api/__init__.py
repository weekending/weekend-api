from fastapi import APIRouter

from .auth_router import router as auth_router
from .band_router import router as band_router
from .post_router import router as post_router
from .schedule_router import router as schedule_router
from .song_router import router as song_router
from .user_router import router as user_router


router = APIRouter(prefix="/api")
router.include_router(auth_router)
router.include_router(band_router)
router.include_router(post_router)
router.include_router(schedule_router)
router.include_router(song_router)
router.include_router(user_router)
