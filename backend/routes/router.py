from fastapi import APIRouter
from backend.routes import authentication, course, lessons


router = APIRouter(prefix="/api")
router.include_router(authentication.router, tags=["authentication"])
router.include_router(course.router, tags=["courses"])
