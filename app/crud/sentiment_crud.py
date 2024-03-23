from datetime import datetime
from typing import List, Optional

from sqlmodel import select, func
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import DateTime

from app.models.sentiment import Sentiment
from app.models.sentiment_fb import SentimentFacebook


async def get_sentiment_by_period(
    session: AsyncSession,
        code: str,
        start_date: datetime,
        end_date: datetime,
        limit: Optional[int] = 100,
        skip: Optional[int] = 0
) -> List[Sentiment]:
    """
    Get sentiment from the database
    Args:
        session (Session): The session of the database
        code (str): The code of the stock
        start_date (datetime): The start date
        end_date (datetime): The end date
        limit (int): The number of rows to limit
        skip (int): The number of rows to skip
    Returns:
        Optional[Sentiment]: The sentiment
    """
    statement = (
        select(Sentiment)
        .where(Sentiment.code == code)
        .where(Sentiment.date >= start_date)
        .where(Sentiment.date <= end_date)
        .limit(limit)
        .offset(skip)
    )
    result = await session.exec(statement)
    return list(result.all())


async def get_sentiment_fb_by_period(
        session: AsyncSession,
        label: str,
        start_date: datetime,
        end_date: datetime,
        limit: Optional[int] = 100,
        skip: Optional[int] = 0
) -> list[SentimentFacebook]:
    """
    Get sentiment from the database
    Args:
        session (Session): The session of the database
        label (str): The label of the sentiment
        start_date (datetime): The start date
        end_date (datetime): The end date
        limit (int): The number of rows to limit
        skip (int): The number of rows to skip
    Returns:
        Optional[Sentiment]: The sentiment
    """
    if label == "all":
        statement = (
            select(SentimentFacebook)
            .where(func.cast(SentimentFacebook.post_created_date, DateTime) >= start_date)
            .where(func.cast(SentimentFacebook.post_created_date, DateTime) <= end_date)
            .limit(limit)
            .offset(skip)
        )
    else:
        statement = (
            select(SentimentFacebook)
            .where(SentimentFacebook.label == label)
            .where(func.cast(SentimentFacebook.post_created_date, DateTime) >= start_date)
            .where(func.cast(SentimentFacebook.post_created_date, DateTime) <= end_date)
            .limit(limit)
            .offset(skip)
        )
    result = await session.exec(statement)
    return list(result.all())
