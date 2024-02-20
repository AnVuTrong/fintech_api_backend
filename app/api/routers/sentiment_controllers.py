from datetime import datetime
from typing import Optional, List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.db import get_session
from app.models.sentiment import Sentiment
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
