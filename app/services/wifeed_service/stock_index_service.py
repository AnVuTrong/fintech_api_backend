from datetime import datetime
from typing import Optional, Dict

import pandas as pd
from fastapi import HTTPException, status

from app.crud import stock_index_crud
from app.models.stock_index import VietnamIndex
from sqlmodel.ext.asyncio.session import AsyncSession

"""
Vietnam stock index services
"""


async def get_vietnam_index_by_date(
    db: AsyncSession = None,
    code: str = None,
    ngay: str = None,
) -> Optional[float]:
    """
    Retrieve a Vietnam stock market index by date.
    :param db: The database session.
    :param code: The stock index code.
    :param ngay: The date of the stock market index.
    """
    try:
        # Convert the date to the correct format
        ngay_converted = datetime.strptime(ngay, "%Y-%m-%d") if ngay else None
        result = await stock_index_crud.get_vietnam_index(db, code, ngay_converted)
        return result

    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stock index not found",
        ) from e


async def get_all_vietnam_indexes(
    db: AsyncSession = None, code: str = None, skip: int = 0, limit: int = 100
) -> Dict[datetime, Optional[float]]:
    """
    Retrieve all Vietnam stock market indexes.
    :param db: The database session.
    :param code: The stock index code.
    :param skip: The number of items to skip.
    :param limit: The number of items to return.
    """
    result = await stock_index_crud.get_all_vietnam_indexes(db, code, skip, limit)
    return result


async def get_vietnam_index_by_period(
        db: AsyncSession = None,
        start_date: str = None,
        end_date: str = None,
) -> list[VietnamIndex]:
    """
    Retrieve Vietnam stock market indexes by period.
    :param db: The database session.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    """
    # Convert the date to the correct format
    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None
    result = await stock_index_crud.get_vietnam_index_by_period(
        db, start_date, end_date
    )
    return result


async def get_vietnam_index_by_period_new(
    db: AsyncSession = None,
    code: str = None,
    start_date: str = None,
    end_date: str = None,
) -> Dict[datetime, Optional[float]]:
    """
    Retrieve Vietnam stock market indexes by period.
    :param db: The database session.
    :param code: The stock index code.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    """
    # Convert the date to the correct format
    start_date = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None
    result = await stock_index_crud.get_vietnam_index_by_period_new(
        db, code, start_date, end_date
    )
    return result
