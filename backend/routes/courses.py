import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.db import get_db


router = APIRouter(prefix="/courses")


@router.get("/") 
def courses_view(db: Session = Depends(get_db)):
    response = {'message': 'return JSON data'}
    #TODO: Collect all data from databases
    #response = json.dumps(response)
    #response = json.loads(response)
    return response


@router.get("/course/")
def course_view(db: Session = Depends(get_db)):
    response = {'message': 'return JSON data'}
