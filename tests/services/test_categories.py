import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import models
from app.core.impl.services.categories import CategoriesServiceImpl


@pytest.mark.asyncio
async def test_get_all(db_session: AsyncSession):
    ids = [uuid.uuid4() for _ in range(4)]
    categories_names = ["Smartphones", "Laptops", "Watch", "Headphones"]

    categories = [
        models.Category(
            id=id_,
            name=name,
        )
        for id_, name in zip(ids, categories_names)
    ]

    db_session.add_all(categories)
    await db_session.commit()

    service = CategoriesServiceImpl(db_session)

    actual = await service.get_all()

    assert isinstance(actual, list)
    assert [c.id for c in actual] == ids
