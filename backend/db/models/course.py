import sqlalchemy as db
from backend.db.db import Base


class Course(Base):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)

    chapters = db.orm.relationship("Chapter",  backref="course")


class Chapter(Base):
    __tablename__ = "chapters"

    id = db.Column(db.Integer, primary_key=True, index=True)
    index = db.Column(db.Integer)
    percentage = db.Column(db.Integer)

    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))

    lessons = db.orm.relationship("Lesson",  backref="chapter")


class Lesson(Base):
    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True, index=True)
    index = db.Column(db.Integer)

    chapter_id = db.Column(db.Integer, db.ForeignKey("chapters.id"))

    tasks = db.orm.relationship("Task", backref="lesson")

