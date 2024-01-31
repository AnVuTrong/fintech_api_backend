from datetime import datetime
from typing import Optional, List

from fastapi import HTTPException, status

from app.crud import stock_news_crud, market_news_crud
from app.models.news import NewsStock, NewsMarket
from sqlmodel.ext.asyncio.session import AsyncSession

"""
Market news services
"""


async def get_market_news_by_id(
    db: AsyncSession = None, news_id: str = None
) -> NewsMarket:
    """
    Retrieve a Market News by ID.
    :param db: The database session.
    :param news_id: The ID of the Market News.
    """
    try:
        result = await market_news_crud.get_market_news(db, news_id)
        return result
    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found",
        ) from e

async def get_all_market_news(db: AsyncSession = None, skip: int = 0, limit: int = 100, news_id: str = None) -> List[NewsMarket]:
    """
    Retrieve a list of all Market News.
    :param news_id: None
    :param db: The database session.
    :param skip: The number of offset rows.
    :param limit: The number of rows to limit.
    """
    return await market_news_crud.get_market_news_list(db, skip, limit)

async def get_latest_market_news(db: AsyncSession = None) -> NewsMarket:
    """
    Retrieve a Market News by time.
    :param db: The database session.
    """
    try:
        result = await market_news_crud.get_market_news_by_time(db)
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="News not found",
            )
        return result
    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong",
        ) from e


async def get_market_news_date(db: AsyncSession = None) -> Optional[datetime]:
    try:
        result = await market_news_crud.get_latest_market_news_date(db)
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="News not found",
            )
        return result
    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong",
        ) from e


"""
Stock news services
"""


async def get_stock_news_by_id(
    db: AsyncSession = None, news_id: str = None
) -> NewsStock:
    """
    Retrieve a Stock News by ID.
    :param db: The database session.
    :param news_id: The ID of the Stock News.
    """
    try:
        result = await stock_news_crud.get_stock_news(db, news_id)
        return result
    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News not found",
        ) from e


async def get_stock_news_date(db: AsyncSession = None) -> Optional[datetime]:
    try:
        result = await stock_news_crud.get_latest_stock_news_date(db)
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="News not found",
            )
        return result
    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Something went wrong",
        ) from e
