from pydantic import BaseModel

from backend.db.models.task import TaskType


class TaskBase(BaseModel):
    title: str
    description: str
    type: TaskType
    lesson_id: int


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int


class LessonBase(BaseModel):
    index: int
    chapter_id: int


class LessonCreate(LessonBase):
    pass


class Lesson(LessonBase):
    id: int
    tasks: list[Task]


class ChapterBase(BaseModel):
    index: int
    percentage: int
    course_id: int


class ChapterCreate(ChapterBase):
    pass


class Chapter(ChapterBase):
    id: int
    lessons: list[Lesson]


class CourseBase(BaseModel):
    title: str
    description: str


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    chapters: list[Chapter]
