from pydantic import BaseModel

from backend.db.models.task import TaskType


class AnswerBase(BaseModel):
    text: str
    is_right: bool
    question_id: int


class AnswerCreate(AnswerBase):
    pass


class Answer(AnswerBase):
    id: int

    class Config:
        orm_mode = True


class QuestionBase(BaseModel):
    text: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    answers: list[Answer]

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    title: str
    description: str
    type: TaskType
    lesson_id: int


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    questions: list[Question]

    class Config:
        orm_mode = True

