from datetime import datetime

import pandas as pd
from fastapi import HTTPException, status

from app.crud import stock_quote_crud as stock
from app.models.stock_quoting import HistoryQuoting
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_stock_quote_by_date(
    db: AsyncSession = None, code: str = None, ngay: str = None
) -> HistoryQuoting:
    """
    Retrieve stock market quoting by date.
    :param db: The database session.
    :param code: The stock code.
    :param ngay: The date of the quoting.
    """
    ngay_converted = datetime.strptime(ngay, "%Y-%m-%d") if ngay else None
    result = await stock.read_stock_quote(db, code, ngay_converted)
    return result


async def get_all_quoting(
    db: AsyncSession = None, skip: int = 0, limit: int = 100
) -> list[HistoryQuoting]:
    """
    Retrieve all stock market quoting.
    :param db: The database session.
    :param skip: The number of items to skip.
    :param limit: The number of items to return.
    """
    result = await stock.get_all_quoting(db, skip, limit)
    return result


async def get_quoting_by_period(
    db: AsyncSession = None,
    code: str = None,
    start_date: str = None,
    end_date: str = None,
) -> list[HistoryQuoting]:
    """
    Retrieve stock market quoting by period.
    :param db: The database session.
    :param code: The stock code.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    """
    start_date_converted = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date_converted = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None
    result = await stock.get_quoting_by_period(db, code, start_date_converted, end_date_converted)
    return result
