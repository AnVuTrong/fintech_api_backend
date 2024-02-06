from datetime import datetime
from typing import Optional, Dict

from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.db import get_session
from app.models.stock_index import VietnamIndex
from app.services.wifeed_service import stock_index_service

router = APIRouter()


@router.get(
    "/vietnam_index/code={code}&ngay={ngay}",
    response_model=Optional[float],
    status_code=status.HTTP_200_OK,
)
async def get_vietnam_index_by_date(
        db: AsyncSession = Depends(get_session),
        code: str = None,
        ngay: str = None,
):
    """
    Get the Vietnam stock market index by date.
    :param code: The stock index code.
    :param db: The database session.
    :param ngay: The date of the stock market index.
    """
    try:
        return await stock_index_service.get_vietnam_index_by_date(db, code, ngay)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stock index not found",
        ) from e


@router.get(
    "/vietnam_index",
    response_model=Dict[datetime, Optional[float]],
    status_code=status.HTTP_200_OK,
)
async def get_all_vietnam_indexes(
        db: AsyncSession = Depends(get_session),
        code: str = None,
        skip: int = 0,
        limit: int = 100
):
    """
    Get all the Vietnam stock market indexes.
    :param db: The database session.
    :param code: The stock index code.
    :param skip: The number of items to skip.
    :param limit: The number of items to return.
    """
    return await stock_index_service.get_all_vietnam_indexes(db, code, skip, limit)


@router.get(
    "/vietnam_index_by_period/start_date={start_date}&end_date={end_date}",
    response_model=list[VietnamIndex],
    status_code=status.HTTP_200_OK,
)
async def get_vietnam_index_by_period(
        start_date,
        end_date,
        db: AsyncSession = Depends(get_session),
):
    """
    Get the Vietnam stock market index by period.
    :param db: The database session.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    """
    return await stock_index_service.get_vietnam_index_by_period(db, start_date, end_date)


@router.get(
    "/vietnam_index_by_period_news/start_date={start_date}&end_date={end_date}",
    response_model=Dict[datetime, Optional[float]],
    status_code=status.HTTP_200_OK,
)
async def get_vietnam_index_by_period_new(
        db: AsyncSession = Depends(get_session),
        code: str = None,
        start_date: str = None,
        end_date: str = None,
):
    """
    Get the Vietnam stock market index by period.
    :param db: The database session.
    :param code: The stock index code.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    """
    return await stock_index_service.get_vietnam_index_by_period_new(db, code, start_date, end_date)
