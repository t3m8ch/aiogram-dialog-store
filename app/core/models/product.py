import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as psql
from sqlalchemy.orm import relationship

from .base import ModelCommonMixin, Base


class Product(ModelCommonMixin, Base):
    __tablename__ = "product"

    name = sa.Column(sa.Unicode(length=100), nullable=False)
    product_code = sa.Column(sa.String(length=16), nullable=False)
    description = sa.Column(sa.UnicodeText, nullable=True)
    characteristics = sa.Column(psql.JSONB, nullable=True)
    price = sa.Column(sa.Numeric(scale=2, precision=14), nullable=False)
    photo_file_id = sa.Column(sa.String(length=100), nullable=True)

    category_id = sa.Column(
        psql.UUID(as_uuid=True),
        sa.ForeignKey("product_category.id"),
        nullable=False
    )
    category = relationship("ProductCategory", back_populates="products")
