from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    full_name: Union[str, None] = None
    active: bool = True
