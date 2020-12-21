from fastapi import APIRouter
from src.app.user.endpoint import user


api_router = APIRouter()
api_router.include_router(user.user_router, prefix="/user")
