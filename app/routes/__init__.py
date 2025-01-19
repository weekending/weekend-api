from fastapi import APIRouter

from .home import router as home_router
from .song import router as song_router


router = APIRouter()
router.include_router(home_router)
router.include_router(song_router)
