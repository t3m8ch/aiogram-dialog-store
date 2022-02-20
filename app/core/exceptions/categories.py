import uuid
from dataclasses import dataclass


@dataclass
class CategoryIsNotExists(Exception):
    category_id: uuid.UUID
