from decimal import Decimal
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String, Numeric, CheckConstraint

__all__ = (
    'Product',
    'Service',
)

from flaskr import db
from flaskr.models.mixins import CreatedUpdatedDateTimeMixin


class BaseProductService:
    organization_id: Mapped[int] = mapped_column(ForeignKey('organizations.id'))
    counterparty_id: Mapped[int| None] = mapped_column(ForeignKey('counterparty.id'), nullable=True)
    units_of_measurement_id: Mapped[int] = mapped_column(ForeignKey('units_of_measurement.id'))
    article: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(50))
    multiplicity: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=1)


class Product(BaseProductService, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'product'

    document_products: Mapped[List["DocumentItem"]] = relationship(back_populates="product")
    purchase_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    selling_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    minimum_stock: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    __table_args__ = (
        CheckConstraint("multiplicity >= 0", name="ck_product_multiplicity_positive"),
        CheckConstraint("article >= 0", name="ck_product_article_positive"),
        CheckConstraint("purchase_price >= 0", name="ck_product_purchase_price_positive"),
        CheckConstraint("selling_price >= 0", name="ck_product_selling_price_positive"),
        CheckConstraint("minimum_stock >= 0", name="ck_product_minimum_stock_positive"),
    )

class Service(BaseProductService, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'service'

    document_services: Mapped[List["DocumentItem"]] = relationship(back_populates="service")
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    __table_args__ = (
        CheckConstraint("multiplicity >= 0", name="ck_service_multiplicity_positive"),
        CheckConstraint("article >= 0", name="ck_service_article_positive"),
        CheckConstraint("price >= 0", name="ck_service_price_positive"),
    )