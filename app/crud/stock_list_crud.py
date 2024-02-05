import uuid
from datetime import datetime
from typing import List, Optional

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.stock_list import StockList


async def get_all_stock_list(session: AsyncSession) -> List[StockList]:
    statement = select(StockList)
    result = await session.exec(statement)
    return list(result.all())
