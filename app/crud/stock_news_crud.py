import uuid
from datetime import datetime
from typing import List, Optional
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from app.models.news import NewsStock


async def create_stock_news(session: AsyncSession, news: NewsStock) -> NewsStock:
    if news.id is None:
        news.id = str(uuid.uuid4())

    session.add(news)
    await session.commit()
    await session.refresh(news)
    return news


async def get_stock_news(session: AsyncSession, id: str) -> Optional[NewsStock]:
    statement = select(NewsStock).where(NewsStock.id == id)
    result = (await session.exec(statement)).first()
    return result


async def get_latest_stock_news_date(session: AsyncSession) -> Optional[datetime]:
    statement = select(NewsStock.time).order_by(NewsStock.time.desc()).limit(1)
    result = await session.exec(statement)
    latest_date_record = result.first()
    return latest_date_record if latest_date_record else None


async def get_stock_news_list_by_entity(
    session: AsyncSession, entity_id: str, skip: int = 0, limit: int = 100
) -> List[NewsStock]:
    statement = (
        select(NewsStock)
        .where(NewsStock.entity_id == entity_id)
        .offset(skip)
        .limit(limit)
    )
    result = await session.exec(statement)
    return list(result.all())


async def get_stock_news_list(
    session: AsyncSession, skip: int = 0, limit: int = 100
) -> List[NewsStock]:
    statement = select(NewsStock).offset(skip).limit(limit)
    result = await session.exec(statement)
    return list(result.all())


async def update_stock_news(
    session: AsyncSession, id: str, news: NewsStock
) -> NewsStock:
    statement = select(NewsStock).where(NewsStock.id == id)
    result = (await session.exec(statement)).first()
    for var, value in vars(news).items():
        setattr(result, var, value)
    session.add(result)
    await session.commit()
    await session.refresh(result)
    return result


async def delete_stock_news(session: AsyncSession, id: str) -> NewsStock:
    statement = select(NewsStock).where(NewsStock.id == id)
    result = (await session.exec(statement)).first()
    await session.delete(result)
    await session.commit()
    return result
