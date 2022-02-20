import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import exceptions
from app.core import models
from app.core.impl.services.products import ProductsServiceImpl


@pytest.mark.asyncio
async def test_get_by_category_id(db_session: AsyncSession):
    smartphones_category_id = uuid.uuid4()
    gpu_category_id = uuid.uuid4()

    ids = [uuid.uuid4() for _ in range(5)]

    categories = [
        models.ProductCategory(
            id=smartphones_category_id,
            name="Smartphones",
            products=[
                models.Product(
                    id=ids[0],
                    name="IPhone 13",
                    product_code="abc1",
                    characteristics={"CPU": "A15 Bionic"},
                    price=1499.99,
                ),
                models.Product(
                    id=ids[1],
                    name="Redmi 10 Pro",
                    product_code="abc2",
                    price=249.99,
                ),
            ]
        ),
        models.ProductCategory(
            id=gpu_category_id,
            name="GPU",
            products=[
                models.Product(
                    id=ids[2],
                    name="Palit GTX 1060",
                    product_code="gpu1",
                    characteristics={"Memory": 6},
                    price=2999.99,
                ),
                models.Product(
                    id=ids[3],
                    name="RTX 2060 Super",
                    product_code="gpu2",
                    price=3999.99,
                ),
                models.Product(
                    id=ids[4],
                    name="RTX 3070 TI",
                    product_code="gpu3",
                    price=4999.99,
                ),
            ]
        ),
    ]

    db_session.add_all(categories)
    await db_session.commit()

    service = ProductsServiceImpl(db_session)

    actual_1 = await service.get_by_category_id(smartphones_category_id)
    actual_2 = await service.get_by_category_id(gpu_category_id)

    assert isinstance(actual_1, list)
    assert [p.id for p in actual_1] == [ids[0], ids[1]]

    assert isinstance(actual_2, list)
    assert [p.id for p in actual_2] == [ids[2], ids[3], ids[4]]


@pytest.mark.asyncio
async def test_get_by_category_id_if_category_is_not_exists(
        db_session: AsyncSession
):
    actual_category_id = uuid.uuid4()

    categories = [
        models.ProductCategory(
            id=actual_category_id,
            name="Smartphones",
            products=[
                models.Product(
                    name="IPhone 13",
                    product_code="abc1",
                    characteristics={"CPU": "A15 Bionic"},
                    price=1499.99,
                ),
                models.Product(
                    name="Redmi 10 Pro",
                    product_code="abc2",
                    price=249.99,
                ),
            ]
        ),
    ]

    db_session.add_all(categories)
    await db_session.commit()

    service = ProductsServiceImpl(db_session)
    category_id = uuid.uuid4()

    try:
        await service.get_by_category_id(category_id)
    except exceptions.CategoryIsNotExists as e:
        assert e.category_id == category_id
    else:
        assert False


@pytest.mark.asyncio
async def test_get_by_category_id_if_there_are_no_products_in_category(
        db_session: AsyncSession
):
    category_id = uuid.uuid4()

    categories = [
        models.ProductCategory(
            id=category_id,
            name="Smartphones",
            products=[]
        ),
    ]

    db_session.add_all(categories)
    await db_session.commit()

    service = ProductsServiceImpl(db_session)

    actual = await service.get_by_category_id(category_id)

    assert actual == []
