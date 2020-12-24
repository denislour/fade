from typing import List

from fastapi import APIRouter
from src.app.user import schemas, services

user_router = APIRouter()


@user_router.get("/me")
async def user_me():
    return {"Result": "Current Users"}


@user_router.get("", response_model=List[schemas.UserPublic])
async def get_all():
    return await services.user_service.all()


@user_router.get("/{pk}", response_model=schemas.UserInDB)
async def get_single_user(pk: int):
    return await services.user_service.get(id=pk)


@user_router.post("", response_model=schemas.UserBaseInDB)
async def create_user(schema: schemas.UserCreate):
    return await services.user_service.create_user(schema)


@user_router.post("/{pk}", response_model=schemas.UserInDB)
async def update_user(pk: int, schema: schemas.UserUpdate):
    return await services.user_service.update(schema=schema, id=pk)


@user_router.delete("/pk", status_code=204)
async def delete_user(pk: int):
    return await services.user_service.delete(id=pk)
