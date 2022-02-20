import uuid
from typing import Protocol

from app.core.models import Product


class ProductsService(Protocol):
    async def get_by_category_id(self, category_id: uuid.UUID) -> list[Product]:
        ...
