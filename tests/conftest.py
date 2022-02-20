import asyncio
import os

import pytest
import pytest_asyncio
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    AsyncEngine
)

from app.core.models import Base

load_dotenv(".testing.env")


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def db_engine():
    if "DB_URL" not in os.environ:
        skip_reason_message = (
            f"Environment var with name 'DB_URL' is not provided."
        )
        pytest.skip(msg=skip_reason_message)

    engine = create_async_engine(os.environ["DB_URL"])

    try:
        yield engine
    finally:
        await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def db_session(db_engine: AsyncEngine):
    async with db_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    session = AsyncSession(db_engine)

    try:
        yield session
    finally:
        await session.close()
        async with db_engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
