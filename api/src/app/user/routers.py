from fastapi import APIRouter
from src.app.user import schemas, services

user_router = APIRouter()


@user_router.get("/me")
async def user_me():
    return {"Result": "Current Users"}


@user_router.post("", response_model=schemas.UserBaseInDB)
async def create_user(schema: schemas.UserCreate):
    return await services.user_service.create_user(schema)
