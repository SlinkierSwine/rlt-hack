from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.schemas import user as schema
from backend.db.models import user as model
from backend.db.crud import user as crud
from backend.db.db import get_db


router = APIRouter()


@router.post("/register/", response_model=schema.User)
def create(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email) 
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    print(user)
    return crud.create_user(db=db, user=user)

