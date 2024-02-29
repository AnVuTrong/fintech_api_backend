from datetime import datetime

from fastapi import HTTPException, status

from app.crud import stock_list_crud
from app.models.stock_list import StockList
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_all_stock_list(db: AsyncSession = None) -> list[StockList]:
    """
    Retrieve all stock market company information.
    :param db: The database session.
    """
    result = await stock_list_crud.get_all_stock_list(db)
    return result


async def get_stock_info_by_code(db: AsyncSession = None, stock_code: str = None) -> StockList:
    """
    Retrieve stock market company information by stock code.
    :param db: The database session.
    :param stock_code: The stock code.
    """
    result = await stock_list_crud.get_stock_info_by_code(db, stock_code)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Stock code {stock_code} not found."
        )
    return result
