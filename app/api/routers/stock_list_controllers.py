from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.db import get_session

from app.models.stock_list import StockList
from app.services.wifeed_service import stock_list_service

router = APIRouter()


@router.get(
    "/stock_list",
    response_model=list[StockList],
    status_code=status.HTTP_200_OK,
)
async def get_all_stock_list(db: AsyncSession = Depends(get_session)):
    """
    Get all the stock list.
    :param db: The database session.
    """
    return await stock_list_service.get_all_stock_list(db)


@router.get(
    "/stock_list/{stock_code}",
    response_model=StockList,
    status_code=status.HTTP_200_OK,
)
async def get_stock_info_by_code(stock_code: str, db: AsyncSession = Depends(get_session)):
    """
    Get a stock list by stock code.
    :param stock_code: The stock code.
    :param db: The database session.
    """
    return await stock_list_service.get_stock_info_by_code(db, stock_code)
