from decimal import Decimal
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Enum, ForeignKey, String, Numeric, CheckConstraint

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

    purchase_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    selling_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    minimum_stock: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    goods_received_notes: Mapped[List["GoodsReceivedNote"]] = relationship(
        back_populates="products",
        secondary="goods_received_note_product_association"
    )
    goods_received_note_associations: Mapped[List["GoodsReceivedNoteProductAssociation"]] = relationship(
        back_populates="product"
    )

    orders: Mapped[List["Order"]] = relationship(
        back_populates="products",
        secondary="order_product_association"
    )
    order_associations: Mapped[List["OrderProductAssociation"]] = relationship(
        back_populates="product"
    )

    invoices: Mapped[List["Invoice"]] = relationship(
        back_populates="products",
        secondary="invoice_product_association"
    )
    invoice_associations: Mapped[List["InvoiceProductAssociation"]] = relationship(
        back_populates="product"
    )

    goods_delivery_notes: Mapped[List["GoodsDeliveryNote"]] = relationship(
        back_populates="products",
        secondary="goods_delivery_note_product_association"
    )
    goods_delivery_note_associations: Mapped[List["GoodsDeliveryNoteProductAssociation"]] = relationship(
        back_populates="product"
    )

    tax_invoices: Mapped[List["TaxInvoice"]] = relationship(
        back_populates="products",
        secondary="tax_invoice_product_association"
    )
    tax_invoice_associations: Mapped[List["TaxInvoiceProductAssociation"]] = relationship(
        back_populates="product"
    )

    __table_args__ = (
        CheckConstraint("multiplicity >= 0", name="ck_product_multiplicity_positive"),
        CheckConstraint("article >= 0", name="ck_product_article_positive"),
        CheckConstraint("purchase_price >= 0", name="ck_product_purchase_price_positive"),
        CheckConstraint("selling_price >= 0", name="ck_product_selling_price_positive"),
        CheckConstraint("minimum_stock >= 0", name="ck_product_minimum_stock_positive"),
    )

class Service(BaseProductService, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'services'

    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    __table_args__ = (
        CheckConstraint("multiplicity >= 0", name="ck_service_multiplicity_positive"),
        CheckConstraint("article >= 0", name="ck_service_article_positive"),
        CheckConstraint("price >= 0", name="ck_service_price_positive"),
    )