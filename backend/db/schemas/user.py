from datetime import datetime
from typing import Union
from pydantic import BaseModel


class BaseUserBase(BaseModel):
    email: str
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
