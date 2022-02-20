import asyncio

from sqlalchemy.ext.asyncio import create_async_engine

from app.core.models import Base
from app.init.config import load_config, DBScriptsConfig

_config = load_config(DBScriptsConfig)
_engine = create_async_engine(_config.db.url, echo=True)


async def _init_db_async():
    async with _engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    await _engine.dispose()


def init_db():
    asyncio.run(_init_db_async())


async def _drop_db_async():
    async with _engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)

    await _engine.dispose()


def drop_db():
    asyncio.run(_drop_db_async())
