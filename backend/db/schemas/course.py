from pydantic import BaseModel

from backend.db.schemas.task import Task



class LessonBase(BaseModel):
    index: int
    chapter_id: int


class LessonCreate(LessonBase):
    pass


class Lesson(LessonBase):
    id: int
    tasks: list[Task]

    class Config:
        orm_mode = True


class ChapterBase(BaseModel):
    index: int
    percentage: int
    course_id: int


class ChapterCreate(ChapterBase):
    pass


class Chapter(ChapterBase):
    id: int
    lessons: list[Lesson]

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    title: str
    description: str | None


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    chapters: list[Chapter]

    class Config:
        orm_mode = True
