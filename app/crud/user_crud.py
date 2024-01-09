from typing import Optional

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.user import AdminUser


async def get_user_by_id(session: AsyncSession, user_id: int) -> Optional[AdminUser]:
    statement = select(AdminUser).where(AdminUser.id == user_id)
    result = (await session.exec(statement)).first()
    return result