import uuid

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import exceptions
from app.core.models import Product, Category


class ProductsServiceImpl:
    def __init__(self, alchemy_session: AsyncSession):
        self._session = alchemy_session

    async def get_by_category_id(self, category_id: uuid.UUID) -> list[Product]:
        if not await self._category_is_exists(category_id):
            raise exceptions.CategoryIsNotExists(category_id)

        return (await self._session.scalars(
            sa.select(Product).where(Product.category_id == category_id)
        )).all()

    async def _category_is_exists(self, category_id: uuid.UUID):
        return await self._session.scalar(
            sa.select(sa.func.count()).where(Category.id == category_id)
        ) > 0
