from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: Optional[str] = None


class UserPublic(UserBase):
    id: int

    class Config:
        orm_mode = True
