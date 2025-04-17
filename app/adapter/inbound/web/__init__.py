from fastapi import APIRouter

from .document_router import router as document_router
from .home_router import router as home_router


router = APIRouter()
router.include_router(document_router)
router.include_router(home_router)
