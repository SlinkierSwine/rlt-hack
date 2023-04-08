from enum import Enum
import sqlalchemy as db
from backend.db.db import Base


class TaskType(Enum):
    theory = 0
    test = 1
    input = 1


class Task(Base):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    type = db.Column(db.Enum(TaskType))

    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"))
