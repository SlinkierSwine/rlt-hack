from datetime import datetime
from pydantic import BaseModel, EmailStr


class BaseUserBase(BaseModel):
    email: EmailStr
    name: str
    surname: str
    middlename: str


class BaseUserCreate(BaseUserBase):
    password: str


class BaseUser(BaseUserBase):
    id: int
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class UserCreate(BaseUserCreate):
    pass


class User(BaseModel):
    id: int
    experience: int
    rating: int
    base_user: BaseUser

    class Config:
        orm_mode = True
