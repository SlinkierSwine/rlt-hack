from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.schemas import course as schema
from backend.db.models import course as model
from backend.db.crud import course as crud
from backend.db.db import get_db
import json


router = APIRouter(prefix="/courses")

@router.get("/")
def courses_view(course: schema.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, id=course.id)
    response = {'message': db_course}
    return response

@router.get("/course/")
def course_view(course: schema.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, id=course.id)
    response = {'message': db_course}
    return response
