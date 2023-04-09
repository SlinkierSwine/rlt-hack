from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.schemas import course as schema
from backend.db.models import course as model
from backend.db.crud import course as crud
from backend.db.db import get_db
from . import lessons, chapters
import json


router = APIRouter(prefix="/courses")
router.include_router(lessons.router, tags=["lessons"])
router.include_router(chapters.router, tags=["chapters"])

@router.get("/", response_model=list[schema.Course])
def courses_view(db: Session = Depends(get_db)):
    db_courses = crud.get_all_courses(db)
    print(db_courses)
    return db_courses

@router.get("/course/", response_model=schema.Course | dict)
def course_view(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    return db_course or {}
