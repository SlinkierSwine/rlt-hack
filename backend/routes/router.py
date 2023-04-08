from fastapi import APIRouter
from backend.routes import authentication
from backend.routes import courses


router = APIRouter(prefix="/api")
router.include_router(authentication.router, tags=["authentication"])
router.include_router(courses.router, tags=["courses"])
