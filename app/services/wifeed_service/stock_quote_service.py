from datetime import datetime

from fastapi import HTTPException, status

from app.crud import stock_quote_crud
from app.models.stock_quoting import HistoryQuoting
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_stock_quote_by_date(
        db: AsyncSession = None, ngay: str = None, code: str = None
) -> HistoryQuoting:
    try:
        # Convert the date to the correct format
        ngay_converted = datetime.strptime(ngay, "%Y-%m-%d") if ngay else None
        result = await stock_quote_crud.read_stock_quote(db, code, ngay_converted)
        return result

    except Exception as e:
        print("error is:", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Stock quote not found",
        ) from e


async def get_all_stock_quote(
        db: AsyncSession = None, skip: int = 0, limit: int = 100, code: str = None
) -> list[HistoryQuoting]:
    """
    Retrieve all stock market quoting.
    :param db: The database session.
    :param skip: The number of items to skip.
    :param limit: The number of items to return.
    :param code: The stock code.
    """
    result = await stock_quote_crud.get_all_stock_quote(db, skip, limit, code)
    return result


async def get_stock_quote_by_period(
        db: AsyncSession = None,
        start_date: str = None,
        end_date: str = None,
        code: str = None
) -> list[HistoryQuoting]:
    """
    Retrieve the stock market index by period.
    :param db: The database session.
    :param start_date: The start date of the period.
    :param end_date: The end date of the period.
    :param code: The stock code.
    """
    start_date_converted = datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
    end_date_converted = datetime.strptime(end_date, "%Y-%m-%d") if end_date else None
    result = await stock_quote_crud.get_stock_quote_by_period(db, start_date_converted, end_date_converted, code)
    return result
