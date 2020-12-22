from fastapi import APIRouter
from src.app.user import routers as user


api_router = APIRouter()
api_router.include_router(user.user_router, prefix="/user")
