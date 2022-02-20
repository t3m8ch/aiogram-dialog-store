from typing import Protocol

from app.core.models import ProductCategory


class CategoriesService(Protocol):
    async def get_all(self) -> list[ProductCategory]:
        ...
