from fastapi import APIRouter

from .auth_router import router as auth_router
from .community_router import router as community_router
from .document_router import router as document_router
from .home_router import router as home_router
from .schedule_router import router as scheduler_router
from .setting_router import router as setting_router
from .song_router import router as song_router


router = APIRouter(include_in_schema=False)
router.include_router(auth_router)
router.include_router(community_router)
router.include_router(document_router)
router.include_router(home_router)
router.include_router(scheduler_router)
router.include_router(setting_router)
router.include_router(song_router)
