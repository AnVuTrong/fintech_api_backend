from fastapi import APIRouter
from app.api.routers import (
    news_controllers,
    user_controllers,
    index_quoting_controllers,
    stock_quote_controllers,
    stock_list_controllers,
    sentiment_controllers,
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

api_router.include_router(
    stock_quote_controllers.router, prefix="/stock_quoting", tags=["Stock Quoting"]
)

api_router.include_router(
    stock_list_controllers.router, prefix="/stock_list", tags=["Stock List"]
)

api_router.include_router(
    sentiment_controllers.router, prefix="/sentiment", tags=["Sentiment"]
)
