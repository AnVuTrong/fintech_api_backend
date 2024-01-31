from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.db import get_session
from app.models.news import NewsStock, NewsMarket
from app.services.wifeed_service import news_service

router = APIRouter()

@router.get(
    "/market/{news_id}",
    response_model=NewsMarket,
    status_code=status.HTTP_200_OK,
)
async def get_market_news_by_id(news_id, db: AsyncSession = Depends(get_session)):
    """
    Get a market new.
    :param db: The database session.
    :param news_id: The ID of the Market News.
    """
    try:
        return await news_service.get_market_news_by_id(db, news_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found",
        ) from e

@router.get(
    "/market/",
    response_model=list[NewsMarket],
    status_code=status.HTTP_200_OK,
)
async def get_all_market_news(
    db: AsyncSession = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
):
    """
    Get a list of all market news, with limiter.
    :param skip: The number of offset rows.
    :param limit: The number of rows to limit.
    :param db: The database session.
    """
    try:
        return await news_service.get_all_market_news(db, skip, limit)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e

@router.get(
    "/market/period/from-date={from_date}&to-date={to_date}",
    response_model=list[NewsMarket],
    status_code=status.HTTP_200_OK,
)
async def get_market_news_by_date(
    from_date: str,
    to_date: str,
    db: AsyncSession = Depends(get_session),
):
    """
    Get a list of market news by period.
    :param from_date: The start date.
    :param to_date: The end date.
    :param db: The database session.
    """
    try:
        return await news_service.get_market_news_by_period(db, from_date, to_date)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e

@router.get(
    "/market/market_news_latest/latest",
    response_model=NewsMarket,
    status_code=status.HTTP_200_OK,
)
async def get_latest_market_news(
    db: AsyncSession = Depends(get_session),
):
    """
    Get the latest date of the market news.
    :param db: The database session.
    """
    try:
        return await news_service.get_latest_market_news(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Server is not available",
        ) from e

@router.get(
    "/stock/{news_id}",
    response_model=NewsStock,
    status_code=status.HTTP_200_OK,
)
async def get_stock_news_by_id(
    news_id,
    db: AsyncSession = Depends(get_session),
):
    """
    Retrieve a Stock New by ID.
    :param db: The database session.
    :param news_id: The ID of the Stock News.
    """

    try:
        return await news_service.get_stock_news_by_id(db, news_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found",
        ) from e
