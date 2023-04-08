from pydantic import BaseModel

from backend.db.schemas.user import BaseUserCreate, BaseUser


class CompanyBase(BaseModel):
    name: str


class CompanyCreate(CompanyBase):
    pass


class Company(CompanyBase):
    id: int
    company_moderators: list

    class Config:
        orm_mode = True


class CompanyModeratorCreate(BaseUserCreate):
    company_id: int


class CompanyModerator(BaseModel):
    id: int
    company: Company
    base_user: BaseUser

    class Config:
        orm_mode = True
