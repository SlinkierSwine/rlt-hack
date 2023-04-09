from pydantic import BaseModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.schemas import course as schema
from backend.db.models import course as model
from backend.db.crud import course as crud
from backend.db.db import get_db
import json


router = APIRouter(prefix="/lesson/")

@router.get("/")
def lesson_page(course: schema.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_lesson(db, id=course.id)
    response = {'message': db_course}
    return response


class TaskRequest(BaseModel):
    """
    Request model for course post view.
    """
    finished_button = False


@router.post("/")
def change_task(course: schema.CourseCreate, db: Session = Depends(get_db), finished_button: BaseModel = False) -> dict:
    db_course = crud.get_lesson(db, id=course.id)
    response = {'message': db_course}
    #TODO: Update data in database
    if not finished_button:
        #TODO: Collect all data from the database
        #response = json.dumps(response)
        #response = json.loads(response)
        return response