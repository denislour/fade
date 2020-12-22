from fastapi import APIRouter
from src.app.user import models, schemas

user_router = APIRouter()


@user_router.get("/me")
async def user_me():
    return {"Result": "Current Users"}
