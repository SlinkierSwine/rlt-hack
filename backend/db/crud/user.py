from sqlalchemy.orm import Session
from backend.db.schemas import user as schema
from backend.db.models import user as model


def create_user(db: Session, user: schema.BaseUserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = model.BaseUser(email=user.email, hashed_password=fake_hashed_password, name=user.name, surname=user.surname, middlename=user.middlename)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def get_user(db: Session, user_id: int):
#     return db.query(model.User).filter(model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(model.BaseUser).filter(model.BaseUser.email == email).first()


