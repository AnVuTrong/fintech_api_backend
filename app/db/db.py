

import os

from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.config import settings


def get_db_url():
    """
    Returns the URL for the database.

    Returns:
        str: The URL for the database.

    """
    # Check if it is running in container mode
    if os.getenv("IS_CONTAINER") in ["True", "true"]:
        db_url = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@postgres:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
    else:
        db_url = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@localhost:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

    print(f"Connecting to database at {db_url}")
    return db_url


engine = create_async_engine(get_db_url(), echo=True, pool_pre_ping=True, future=True)
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False, future=True
)

async def get_session() -> AsyncSession:
    """
    Returns a context manager that provides a database session.

    Returns:
        AsyncSession: A context manager that provides a database session.

    """
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()