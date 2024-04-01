from datetime import datetime
from typing import List, Optional

from sqlmodel import select, func
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import DateTime

from app.models.sentiment import Sentiment
from app.models.sentiment_fb import SentimentFacebook, SentimentUEHFB, SentimentUEHGG


async def get_sentiment_by_period(
    session: AsyncSession,
        code: str,
        start_date: datetime,
        end_date: datetime,
        limit: Optional[int] = 100,
        skip: Optional[int] = 0
) -> List[Sentiment]:
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
    if label == "all":
        statement = (
            select(SentimentFacebook)
            .where(SentimentFacebook.created_at >= start_date)
            .where(SentimentFacebook.created_at <= end_date)
            .limit(limit)
            .offset(skip)
        )
    else:
        statement = (
            select(SentimentFacebook)
            .where(SentimentFacebook.label == label)
            .where(SentimentFacebook.created_at >= start_date)
            .where(SentimentFacebook.created_at <= end_date)
            .limit(limit)
            .offset(skip)
        )
    result = await session.exec(statement)
    return list(result.all())


async def get_sentiment_ueh_fb_by_period(
        session: AsyncSession,
        label: str,
        start_date: datetime,
        end_date: datetime,
        limit: Optional[int] = 100,
        skip: Optional[int] = 0
) -> list[SentimentUEHFB]:
    if label == "all":
        statement = (
            select(SentimentUEHFB)
            .where(SentimentUEHFB.post_created_at >= start_date)
            .where(SentimentUEHFB.post_created_at <= end_date)
            .limit(limit)
            .offset(skip)
        )
    else:
        statement = (
            select(SentimentUEHFB)
            .where(SentimentUEHFB.label == label)
            .where(SentimentUEHFB.post_created_at >= start_date)
            .where(SentimentUEHFB.post_created_at <= end_date)
            .limit(limit)
            .offset(skip)
        )
    result = await session.exec(statement)
    return list(result.all())


async def get_sentiment_ueh_gg_by_period(
        session: AsyncSession,
        label: str,
        start_date: datetime,
        end_date: datetime,
        limit: Optional[int] = 100,
        skip: Optional[int] = 0
) -> list[SentimentUEHGG]:
    if label == "all":
        statement = (
            select(SentimentUEHGG)
            .where(SentimentUEHGG.post_created_at >= start_date)
            .where(SentimentUEHGG.post_created_at <= end_date)
            .limit(limit)
            .offset(skip)
        )
    else:
        statement = (
            select(SentimentUEHGG)
            .where(SentimentUEHGG.label == label)
            .where(SentimentUEHGG.post_created_at >= start_date)
            .where(SentimentUEHGG.post_created_at <= end_date)
            .limit(limit)
            .offset(skip)
        )
    result = await session.exec(statement)
    return list(result.all())
