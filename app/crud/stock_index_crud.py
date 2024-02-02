from datetime import datetime
from typing import List, Optional

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


async def get_vietnam_index(session: AsyncSession, ngay: datetime) -> Optional[VietnamIndex]:
    statement = select(VietnamIndex).where(VietnamIndex.ngay == ngay)
    result = await session.exec(statement)
    return result.first()


async def get_all_vietnam_indexes(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[VietnamIndex]:
    statement = select(VietnamIndex).offset(skip).limit(limit)
    result = await session.exec(statement)
    return list(result.all())


async def get_vietnam_index_by_period(
        session: AsyncSession,
        start_date: datetime,
        end_date: datetime,
) -> List[VietnamIndex]:
    statement = (
        select(VietnamIndex)
        .where(VietnamIndex.ngay >= start_date)
        .where(VietnamIndex.ngay <= end_date)
        .order_by(VietnamIndex.ngay)
    )
    result = await session.exec(statement)
    return list(result.all())


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
