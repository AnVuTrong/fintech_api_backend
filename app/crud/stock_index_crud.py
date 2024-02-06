from datetime import datetime
from typing import List, Optional, Dict

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.stock_index import VietnamIndex

"""
In this file, we will define the functions CRUD for the vietnam stock market index table using SQLModel.
"""


async def create_vietnam_index(session: AsyncSession, index: VietnamIndex) -> VietnamIndex:
    session.add(index)
    await session.commit()
    return index


async def get_vietnam_index(session: AsyncSession, code: str, ngay: datetime) -> Optional[float]:
    if code not in VietnamIndex.model_fields:
        raise ValueError("Invalid column name")
    column_attribute = getattr(VietnamIndex, code)

    statement = (
        select(column_attribute)
        .where(VietnamIndex.ngay == ngay)
    )
    result = await session.exec(statement)
    return result.first()


async def get_all_vietnam_indexes(
        session: AsyncSession,
        code: str, skip:
        int = 0, limit:
        int = 100
) -> Dict[datetime, Optional[float]]:
    if code not in VietnamIndex.model_fields:
        raise ValueError("Invalid column name")
    column_attribute = getattr(VietnamIndex, code)
    date_column = VietnamIndex.ngay
    statement = select(date_column, column_attribute).offset(skip).limit(limit)
    result = await session.execute(statement)
    rows = result.all()
    index_date_mapping = {row[0]: row[1] for row in rows}
    return index_date_mapping


async def get_vietnam_index_by_period(
        session: AsyncSession,
        code: str,
        start_date: datetime,
        end_date: datetime,
) -> Dict[datetime, Optional[float]]:

    if code not in VietnamIndex.model_fields:
        raise ValueError("Invalid column name")
    column_attribute = getattr(VietnamIndex, code)
    date_column = VietnamIndex.ngay
    statement = (
        select(date_column, column_attribute)
        .where(VietnamIndex.ngay >= start_date)
        .where(VietnamIndex.ngay <= end_date)
        .order_by(VietnamIndex.ngay)
    )

    result = await session.execute(statement)
    rows = result.all()
    index_date_mapping = {row[0]: row[1] for row in rows}
    return index_date_mapping


async def update_vietnam_index(session: AsyncSession, index: VietnamIndex) -> VietnamIndex:
    statement = select(VietnamIndex).where(VietnamIndex.ngay == index.ngay)
    result = (await session.exec(statement)).first()

    for var, value in vars(index).items():
        setattr(result, var, value)

    await session.commit()
    await session.refresh(result)
    return result


async def delete_vietnam_index(session: AsyncSession, ngay: datetime):
    statement = select(VietnamIndex).where(VietnamIndex.ngay == ngay)
    result = (await session.exec(statement)).first()
    if result:
        await session.delete(result)
        await session.commit()
    else:
        raise Exception("VietnamIndex not found")
