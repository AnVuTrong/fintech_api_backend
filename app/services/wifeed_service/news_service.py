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

async def get_all_market_news(db: AsyncSession = None, skip: int = 0, limit: int = 100) -> List[NewsMarket]:
    """
    Retrieve a list of all Market News.
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

async def get_market_news_by_period(
        db: AsyncSession = None,
        from_date: str = None,
        to_date: str = None,
        skip: int = 0,
        limit: int = 100
) -> List[NewsMarket]:
    """
    Retrieve a list of Market News by period.
    :param skip: The number of offset rows.
    :param limit: The number of rows to limit.
    :param db: The database session.
    :param from_date: The start date.
    :param to_date: The end date.
    """
    try:
        # Convert the dates from string to datetime
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        to_date = datetime.strptime(to_date, "%Y-%m-%d")

        result = await market_news_crud.get_market_news_by_period(db, from_date, to_date, skip, limit)
        return result

    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
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

async def get_all_stock_news(db: AsyncSession = None, skip: int = 0, limit: int = 100) -> List[NewsStock]:
    """
    Retrieve a list of all Stock News.
    :param db: The database session.
    :param skip: The number of offset rows.
    :param limit: The number of rows to limit.
    """
    return await stock_news_crud.get_stock_news_list(db, skip, limit)

async def get_stock_news_by_period(
    db: AsyncSession = None,
    from_date: str = None,
    to_date: str = None,
    skip: int = 0,
    limit: int = 100,
) -> List[NewsStock]:
    """
    Retrieve a list of Stock News by period.
    :param db: The database session.
    :param from_date: The start date.
    :param to_date: The end date.
    :param skip: The number of offset rows.
    :param limit: The number of rows to limit.
    """
    try:
        # Convert the dates from string to datetime
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        to_date = datetime.strptime(to_date, "%Y-%m-%d")

        result = await stock_news_crud.get_stock_news_by_period(db, from_date, to_date, skip, limit)
        return result
    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e