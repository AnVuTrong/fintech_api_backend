from datetime import datetime
from typing import Optional, List

from fastapi import HTTPException, status

from app.crud import sentiment_crud
from app.models.sentiment import Sentiment
from app.models.sentiment_fb import SentimentFacebook, SentimentUEH
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_sentiment_list(
    db: AsyncSession = None,
    code: str = None,
    start_date: datetime = None,
    end_date: datetime = None,
    limit: Optional[int] = 100,
    skip: Optional[int] = 0,
) -> List[Sentiment]:
    """
    Retrieve a list of Sentiments by code, date and time.
    :param db: The database session.
    :param code: The stock code.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    :param limit: The number of rows to limit.
    :param skip: The number of offset rows.
    """
    try:
        result = await sentiment_crud.get_sentiment_by_period(
            db, code, start_date, end_date, limit, skip
        )
        return result
    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentiment not found",
        ) from e


async def get_sentiment_fb_list(
    db: AsyncSession = None,
    label: str = None,
    start_date: datetime = None,
    end_date: datetime = None,
    limit: Optional[int] = 100,
    skip: Optional[int] = 0,
) -> List[SentimentFacebook]:
    """
    Retrieve a list of Sentiments by label, date and time.
    :param db: The database session.
    :param label: The sentiment label.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    :param limit: The number of rows to limit.
    :param skip: The number of offset rows.
    """
    try:
        result = await sentiment_crud.get_sentiment_fb_by_period(
            db, label, start_date, end_date, limit, skip
        )
        return result
    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentiment not found",
        ) from e


async def get_sentiment_ueh_list(
        db: AsyncSession = None,
        label: str = None,
        start_date: datetime = None,
        end_date: datetime = None,
        limit: Optional[int] = 100,
        skip: Optional[int] = 0,
) -> List[SentimentUEH]:
    """
    Retrieve a list of Sentiments by label, date and time.
    :param db: The database session.
    :param label: The sentiment label.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    :param limit: The number of rows to limit.
    :param skip: The number of offset rows.
    """
    try:
        result = await sentiment_crud.get_sentiment_ueh_by_period(
            db, label, start_date, end_date, limit, skip
        )
        return result
    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentiment not found",
        ) from e
