from fastapi import APIRouter
from app.api.routers import (
    news_controllers,
    user_controllers,
    index_quoting_controllers
)

api_router = APIRouter()


api_router.include_router(
    news_controllers.router, prefix="/news", tags=["News"]
)

api_router.include_router(
    user_controllers.router, prefix="/user", tags=["User"]
)

api_router.include_router(
    index_quoting_controllers.router, prefix="/news", tags=["Index"]
)
