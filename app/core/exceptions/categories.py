import uuid
from dataclasses import dataclass


@dataclass(slots=True)
class CategoryIsNotExists(Exception):
    category_id: uuid.UUID
