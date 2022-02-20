import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import Category


class CategoriesServiceImpl:
    def __init__(self, alchemy_session: AsyncSession):
        self._session = alchemy_session

    async def get_all(self) -> list[Category]:
        return (await self._session.scalars(sa.select(Category))).all()
