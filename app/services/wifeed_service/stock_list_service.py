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
