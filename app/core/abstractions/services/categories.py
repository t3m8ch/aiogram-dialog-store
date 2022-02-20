from typing import Protocol

from app.core.models import Category


class CategoriesService(Protocol):
    async def get_all(self) -> list[Category]:
        ...
