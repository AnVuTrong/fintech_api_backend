from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.db import get_session
from app.models.stock_quoting import HistoryQuoting
from app.services.wifeed_service import stock_quoting_service

router = APIRouter()


@router.get(
    "/history_quoting/code={code}&ngay={ngay}",
    response_model=HistoryQuoting,
    status_code=status.HTTP_200_OK,
)
async def get_stock_quote_by_date(
        code,
        ngay,
        db: AsyncSession = Depends(get_session),
):
    """
    Get stock market quoting by date.
    :param db: The database session.
    :param code: The stock code.
    :param ngay: The date of the quoting.
    """
    return await stock_quoting_service.get_stock_quote_by_date(db, code, ngay)


@router.get(
    "/history_quoting/all/",
    response_model=list[HistoryQuoting],
    status_code=status.HTTP_200_OK,
)
async def get_all_quoting(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    """
    Get all stock markets quoting.
    :param db: The database session.
    :param skip: The number of items to skip.
    :param limit: The number of items to return.
    """
    return await stock_quoting_service.get_all_quoting(db, skip, limit)


@router.get(
    "/history_quoting_by_period/code={code}&start_date={start_date}&end_date={end_date}",
    response_model=list[HistoryQuoting],
    status_code=status.HTTP_200_OK,
)
async def get_quoting_by_period(
        code,
        start_date,
        end_date,
        db: AsyncSession = Depends(get_session),
):
    """
    Get stock market quoting by period.
    :param db: The database session.
    :param code: The stock code.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    """
    return await stock_quoting_service.get_quoting_by_period(db, code, start_date, end_date)
