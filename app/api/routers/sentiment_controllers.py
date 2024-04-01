from datetime import datetime
from typing import Optional, List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.db import get_session
from app.models.sentiment import Sentiment
from app.models.sentiment_fb import SentimentFacebook, SentimentUEH, SentimentUEHResponse, SentimentFBResponse
from app.services.wifeed_service import sentiment_service

router = APIRouter()


@router.get(
    "/sentiment/code={code}&start-date={start_date}&end-date={end_date}&limit={limit}&skip={skip}",
    response_model=List[Sentiment],
    status_code=status.HTTP_200_OK,
)
async def get_sentiment_list(
    code: str,
    start_date: str = None,
    end_date: str = None,
    limit: Optional[int] = 100,
    skip: Optional[int] = 0,
    session: AsyncSession = Depends(get_session),
):
    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None

    sentiment = await sentiment_service.get_sentiment_list(
        session, code, start_date, end_date, limit, skip
    )
    if sentiment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentiment not found",
        )
    return sentiment


@router.get(
    "/sentiment_fb/label={label}&start-date={start_date}&end-date={end_date}&limit={limit}&skip={skip}",
    response_model=List[SentimentFacebook],
    status_code=status.HTTP_200_OK,
)
async def get_sentiment_fb_list(
    label: str,
    start_date: str = None,
    end_date: str = None,
    limit: Optional[int] = 100,
    skip: Optional[int] = 0,
    session: AsyncSession = Depends(get_session),
):
    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None

    sentiment_fb = await sentiment_service.get_sentiment_fb_list(
        session, label, start_date, end_date, limit, skip
    )
    if sentiment_fb is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentiment Facebook not found",
        )
    return sentiment_fb


@router.get(
    "/sentiment_ueh/label={label}&start-date={start_date}&end-date={end_date}&limit={limit}&skip={skip}",
    response_model=List[SentimentUEH],
    status_code=status.HTTP_200_OK,
)
async def get_sentiment_ueh_list(
        label: str,
        start_date: str = None,
        end_date: str = None,
        limit: Optional[int] = 100,
        skip: Optional[int] = 0,
        session: AsyncSession = Depends(get_session),
):
    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None

    sentiment_ueh = await sentiment_service.get_sentiment_ueh_list(
        session, label, start_date, end_date, limit, skip
    )
    if sentiment_ueh is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentiment UEH not found",
        )
    return sentiment_ueh


@router.get(
    "/sentiment_fb_avg/label={label}&start-date={start_date}&end-date={end_date}&limit={limit}&skip={skip}",
    response_model=SentimentFBResponse,
    status_code=status.HTTP_200_OK,
)
async def get_sentiment_fb_list(
        label: str,
        start_date: str = None,
        end_date: str = None,
        limit: Optional[int] = 100,
        skip: Optional[int] = 0,
        session: AsyncSession = Depends(get_session),
):
    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None

    sentiment_fb = await sentiment_service.get_sentiment_fb_list(
        session, label, start_date, end_date, limit, skip
    )
    if not sentiment_fb:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentiment Facebook not found",
        )

    # Calculate the average sentiment
    sentiments = [post.sentiment for post in sentiment_fb if post.sentiment is not None]
    average_sentiment = sum(sentiments) / len(sentiments) if sentiments else None

    # Calculate the weighted average sentiment
    total_weighted_sentiment = 0
    total_interactions = 0
    for post in sentiment_fb:
        if post.sentiment is not None and post.total_interactions is not None:
            try:
                interactions = int(post.total_interactions)
                total_weighted_sentiment += post.sentiment * interactions
                total_interactions += interactions
            except ValueError:
                # Handle cases where total_interactions is not an integer
                continue

    average_weighted_sentiment = (total_weighted_sentiment / total_interactions) if total_interactions > 0 else None

    return SentimentFBResponse(sentiment_facebook_list=sentiment_fb, average_sentiment=average_sentiment,
                               average_weighted_sentiment=average_weighted_sentiment)


@router.get(
    "/sentiment_ueh_avg/label={label}&start-date={start_date}&end-date={end_date}&limit={limit}&skip={skip}",
    response_model=SentimentUEHResponse,
    status_code=status.HTTP_200_OK,
)
async def get_sentiment_fb_list(
        label: str,
        start_date: str = None,
        end_date: str = None,
        limit: Optional[int] = 100,
        skip: Optional[int] = 0,
        session: AsyncSession = Depends(get_session),
):
    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None

    sentiment_ueh = await sentiment_service.get_sentiment_ueh_list(
        session, label, start_date, end_date, limit, skip
    )
    if not sentiment_ueh:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sentiment Facebook not found",
        )

    # Calculate the average sentiment
    sentiments = [post.sentiment for post in sentiment_ueh if post.sentiment is not None]
    average_sentiment = sum(sentiments) / len(sentiments) if sentiments else None

    # Calculate the weighted average sentiment
    total_weighted_sentiment = 0
    total_interactions = 0
    for post in sentiment_ueh:
        if post.sentiment is not None and post.total_interactions is not None:
            try:
                interactions = int(post.total_interactions)
                total_weighted_sentiment += post.sentiment * interactions
                total_interactions += interactions
            except ValueError:
                # Handle cases where total_interactions is not an integer
                continue

    average_weighted_sentiment = (total_weighted_sentiment / total_interactions) if total_interactions > 0 else None

    return SentimentUEHResponse(sentiment_ueh_list=sentiment_ueh, average_sentiment=average_sentiment,
                                average_weighted_sentiment=average_weighted_sentiment)
