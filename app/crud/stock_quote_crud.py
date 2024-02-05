from datetime import datetime
from typing import List, Optional

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.stock_quoting import HistoryQuoting

async def create_stock_quote(session: AsyncSession, quote: HistoryQuoting) -> HistoryQuoting:
    session.add(quote)
    await session.commit()
    await session.refresh(quote)
    return quote

async def read_stock_quote(session: AsyncSession, code: str, ngay: datetime) -> Optional[HistoryQuoting]:
    statement = (
        select(HistoryQuoting).
        where(HistoryQuoting.mack == code).
        where(HistoryQuoting.lastupdate == ngay)
    )
    result = await session.exec(statement)
    return result.first()


async def get_all_quoting(session: AsyncSession, skip: int = 0, limit: int = 100) -> List[HistoryQuoting]:
    statement = select(HistoryQuoting).offset(skip).limit(limit)
    result = await session.exec(statement)
    return list(result.all())

async def get_quoting_by_period(session: AsyncSession, code: str, start_date: datetime, end_date: datetime) -> List[HistoryQuoting]:
    statement = (
        select(HistoryQuoting)
        .where(HistoryQuoting.mack == code)
        .where(HistoryQuoting.ngay >= start_date)
        .where(HistoryQuoting.ngay <= end_date)
        .order_by(HistoryQuoting.ngay)
    )
    result = await session.exec(statement)
    return list(result.all())

async def update_quoting(session: AsyncSession, quoting: HistoryQuoting) -> HistoryQuoting:
    statement = select(HistoryQuoting).where(HistoryQuoting.ngay == quoting.ngay)
    result = (await session.exec(statement)).first()

    for var, value in vars(quoting).items():
        setattr(result, var, value)

    await session.commit()
    await session.refresh(result)
    return result


async def delete_quoting(session: AsyncSession, ngay: datetime):
    statement = select(HistoryQuoting).where(HistoryQuoting.ngay == ngay)
    result = (await session.exec(statement)).first()
    if result:
        await session.delete(result)
        await session.commit()
    else:
        raise Exception("HistoryQuoting not found")