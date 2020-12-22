from typing import Optional
from pydantic import BaseModel, EmailStr
from fastapi import Form
from tortoise.contrib.pydantic import pydantic_model_creator

from src.app.user.models import User


class UserBase(BaseModel):
    first_name: Optional[str] = None


class UserBaseInDB(BaseModel):
    """
        Base properties
    """
    id: int = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class UserCreate(UserBaseInDB):
    """
        Properties for getting through the API
        when creating from the admin panel
    """
    username: str
    email: EmailStr
    password: str
    first_name: str
    avatar: str = None


class UserCreateInRegistration(UserBaseInDB):
    """
        Properties for getting through the API
        when creating from the admin panel
    """
    username: str
    email: EmailStr
    password: str
    first_name: str
    avatar: str = None

    class Config:
        orm_mode = True


class UserUpdate(UserBaseInDB):
    password: Optional[str] = Form(...)


class UserInDB(UserBaseInDB):
    """
        Additional properties stored in DB
    """
    pass


class UserPublic(UserBase):
    id: int

    class Config:
        orm_mode = True


User_G_Pydantic = pydantic_model_creator(User, name='user')
