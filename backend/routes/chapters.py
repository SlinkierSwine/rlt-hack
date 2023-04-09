from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.schemas import course as schema
from backend.db.models import course as model
from backend.db.crud import course as crud
from backend.db.db import get_db
from . import lessons
import json


router = APIRouter(prefix="/chapters")

@router.get("/", response_model=list[schema.Chapter])
def chapters_view(db: Session = Depends(get_db)):
    db_courses = crud.get_all_chapters(db, 1)
    return db_courses

@router.get("/chapter/", response_model=schema.Chapter | dict)
def chapter_view(chapter_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_chapter(db, chapter_id=chapter_id)
    return db_course or {}
