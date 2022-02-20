import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .base import ModelCommonMixin, Base


class Category(ModelCommonMixin, Base):
    __tablename__ = "category"

    name = sa.Column(sa.Unicode(length=100), nullable=False)
    description = sa.Column(sa.UnicodeText, nullable=True)

    products = relationship("Product", back_populates="category")
