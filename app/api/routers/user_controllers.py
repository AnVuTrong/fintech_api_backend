from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db.db import get_session
from app.models.user import AdminUser
from app.crud import user_crud

router = APIRouter()

@router.get(
    "/user/{user_id}",
    response_model=AdminUser,
    status_code=status.HTTP_200_OK,
)
async def get_user_by_id(
    user_id,
    db: AsyncSession = Depends(get_session),
):
    """
    Get a user.
    :param db: The database session.
    :param user_id: The ID of the user.
    """
    try:
        return await user_crud.get_user_by_id(db, user_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        ) from e