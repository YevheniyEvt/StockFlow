from decimal import Decimal
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from sqlalchemy import Integer, ForeignKey, String, Numeric, CheckConstraint

__all__ = (
    'Product',
    'Service',
)

from flaskr import db
from flaskr.core.mixins import CreatedUpdatedDateTimeMixin


class BaseProductService:
    """
    Base class for product and service models.
    
    Contains shared attributes like organization_id, counterparty_id, 
    units_of_measurement_id, article, name, and multiplicity.
    """

    @declared_attr
    def organization_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey('organization.id'))

    @declared_attr
    def counterparty_id(cls) -> Mapped[int | None]:
        return mapped_column(ForeignKey('counterparty.id'), nullable=True)

    @declared_attr
    def units_of_measurement_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey('units_of_measurement.id'))

    @declared_attr
    def units_of_measurement(cls) -> Mapped["UnitsOfMeasurement"]:
        return relationship()

    @declared_attr
    def article(cls) -> Mapped[int]:
        return mapped_column(Integer)

    @declared_attr
    def name(cls) -> Mapped[str]:
        return mapped_column(String(50))

    @declared_attr
    def multiplicity(cls) -> Mapped[Decimal]:
        return mapped_column(Numeric(10, 2), default=1)

    @declared_attr
    def selling_price(cls) -> Mapped[Decimal]:
        return mapped_column(Numeric(10, 2))

class Product(BaseProductService, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'product'

    document_products: Mapped[List["DocumentItem"]] = relationship(back_populates="product")
    minimum_stock: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=1)

    __table_args__ = (
        CheckConstraint("multiplicity >= 0", name="ck_product_multiplicity_positive"),
        CheckConstraint("article >= 0", name="ck_product_article_positive"),
        CheckConstraint("selling_price >= 0", name="ck_product_selling_price_positive"),
        CheckConstraint("minimum_stock >= 0", name="ck_product_minimum_stock_positive"),
    )

class Service(BaseProductService, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'service'

    document_services: Mapped[List["DocumentItem"]] = relationship(back_populates="service")

    __table_args__ = (
        CheckConstraint("multiplicity >= 0", name="ck_service_multiplicity_positive"),
        CheckConstraint("article >= 0", name="ck_service_article_positive"),
        CheckConstraint("selling_price >= 0", name="ck_service_price_positive"),
    )
