from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.db.db import get_db


router = APIRouter(prefix="/lesson/")

@router.get("/")
def lesson_page(db: Session = Depends(get_db)):
    response = {'message': 'return JSON data. Lesson'}
    #TODO: Collect all data from databases
    #response = json.dumps(response)
    #response = json.loads(response)
    return response


class TaskRequest(BaseModel):
    """
    Request model for course post view.
    """
    finished_button = False


@router.post("/")
def change_task(db: Session = Depends(get_db), finished_button: BaseModel = False) -> dict:
    response = {'message': 'return JSON data. Task'}
    #TODO: Update data in database
    if not finished_button:
        #TODO: Collect all data from the database
        #response = json.dumps(response)
        #response = json.loads(response)
        return response
    