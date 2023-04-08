from sqlalchemy.orm import Session
from backend.db.schemas import user as schema
from backend.db.models import user as model


def create_base_user(db: Session, user: schema.BaseUserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_base_user = model.BaseUser(email=user.email, hashed_password=fake_hashed_password, name=user.name, surname=user.surname, middlename=user.middlename)
    db.add(db_base_user)
    db.commit()
    db.refresh(db_base_user)
    return db_base_user


def get_base_user(db: Session, user_id: int):
    return db.query(model.BaseUser).filter(model.BaseUser.id == user_id).first()


def get_base_user_by_email(db: Session, email: str):
    return db.query(model.BaseUser).filter(model.BaseUser.email == email).first()


def create_user(db: Session, user: schema.UserCreate):
    base_user = create_base_user(db, user)
    db_user = model.User(base_user_id=base_user.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.base_user.has(email=email)).first()


