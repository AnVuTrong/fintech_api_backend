import logging
import uuid
from datetime import datetime
from typing import List, Optional

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.news import NewsMarket

"""
In this file, we will define the functions CRUD for the market news table using SQLModel.
"""


async def create_market_news(session: AsyncSession, news: NewsMarket) -> NewsMarket:
    """
    Create news in the database

    Args:
        session (Session): The session of the database
        news (News): The news to create

    Returns:
        News: The created news
    """

    # Make sure that the ID is set
    if news.id is None:
        # Create a UUID for the news as a string
        news.id = str(uuid.uuid4())

    session.add(news)
    await session.commit()
    await session.refresh(news)
    return news


async def get_market_news(session: AsyncSession, id: str) -> Optional[NewsMarket]:
    """
    Get news from the database

    Args:
        session (Session): The session of the database
        id (str): The id of the news

    Returns:
        Optional[NewsMarket]: The news
    """
    statement = select(NewsMarket).where(NewsMarket.id == id)
    result = await session.exec(statement)
    return result.first()


async def get_market_news_by_time(session: AsyncSession) -> Optional[NewsMarket]:
    """
    Get the latest market news by the time

    Args:
        session (Session): The session of the database

    Returns:
        Optional[NewsMarket]: The news
    """

    statement = select(NewsMarket).order_by(NewsMarket.time.desc())
    result = await session.exec(statement)
    return result.first()

async def get_latest_market_news_date(session: AsyncSession) -> Optional[datetime]:
    statement = select(NewsMarket.time).order_by(NewsMarket.time.desc()).limit(1)
    result = await session.exec(statement)
    latest_date_record = result.first()
    return latest_date_record if latest_date_record else None

async def get_market_news_list_by_entity(
    session: AsyncSession, entity_id: str, skip: int = 0, limit: int = 100
) -> List[NewsMarket]:
    """
    Get news from the database

    Args:
        session (Session): The session of the database
        entity_id (str): The id of the entity
        skip (int): The number of rows to skip
        limit (int): The number of rows to limit

    Returns:
        List[News]: The news list of the entity
    """

    statement = (
        select(NewsMarket)
        .where(NewsMarket.entity_id == entity_id)
        .offset(skip)
        .limit(limit)
    )
    result = await session.exec(statement)
    return list(result.all())



async def get_market_news_list(
    session: AsyncSession, skip: int = 0, limit: int = 100, news_id: str = None
) -> List[NewsMarket]:
    """
    Get all news from the database

    Args:
        session (Session): The session of the database
        skip (int): The number of rows to skip
        limit (int): The number of rows to limit
        news_id (str): The id of the news

    Returns:
        List[News]: The news list of the entity
    """
    statement = select(NewsMarket).where(news_id).offset(skip).limit(limit)
    result = await session.exec(statement)
    news_list = list(result.all())
    return news_list

async def update_market_news(session: AsyncSession, id: str, news: NewsMarket) -> NewsMarket:
    """
    Update news in the database

    Args:
        session (Session): The session of the database
        id (str): The id of the news
        news: The news to update

    Returns:
        News: The updated news
    """

    statement = select(NewsMarket).where(NewsMarket.id == id)
    result = (await session.exec(statement)).first()
    for var, value in vars(news).items():
        setattr(result, var, value)
    session.add(result)
    await session.commit()
    await session.refresh(result)
    return result


async def delete_market_news(session: AsyncSession, id: str) -> NewsMarket:
    """
    Delete news from the database

    Args:
        session (Session): The session of the database
        id (str): The id of the news

    Returns:
        News: The deleted news
        :param id:
        :param session:
    """
    statement = select(NewsMarket).where(NewsMarket.id == id)
    result = (await session.exec(statement)).first()
    if result:
        await session.delete(result)
        await session.commit()
    else:
        raise Exception("Market new not found")
