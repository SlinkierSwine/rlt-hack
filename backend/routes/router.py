from fastapi import APIRouter
from backend.routes import authentication


router = APIRouter(prefix="/api")
router.include_router(authentication.router, tags=["authentication"])
