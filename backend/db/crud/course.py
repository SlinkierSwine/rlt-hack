from sqlalchemy.orm import Session
from backend.db.schemas import course as schema
from backend.db.models import course as model


def get_course(db: Session, course_id: int):
    return db.query(model.Course).filter(model.Course.id == course_id).first()


def get_chapter(db: Session, chapter_id: int):
    return db.query(model.Chapter).filter(model.Chapter.id == chapter_id).first()


def get_lesson(db: Session, lesson_id: int):
    return db.query(model.Lesson).filter(model.Lesson.id == lesson_id).first()
