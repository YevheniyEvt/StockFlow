from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from flaskr import db
from flaskr.models.mixins import ItemsMixin


__all__ = (
    'GoodsReceivedNoteProductAssociation',
    'OrderProductAssociation',
    'InvoiceProductAssociation',
    'GoodsDeliveryNoteProductAssociation',
    'TaxInvoiceProductAssociation',
)


class GoodsReceivedNoteProductAssociation(ItemsMixin, db.Model):
    __tablename__ = 'goods_received_note_product_association'

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), primary_key=True)
    goods_received_note_id: Mapped[int] = mapped_column(ForeignKey('goods_received_note.id'), primary_key=True)
    product: Mapped["Product"] = relationship(back_populates="goods_received_note_associations")
    goods_received_note: Mapped["GoodsReceivedNote"] = relationship(back_populates="product_associations")


class OrderProductAssociation(ItemsMixin, db.Model):
    __tablename__ = 'order_product_association'

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('order.id'))
    product: Mapped["Product"] = relationship(back_populates="order_associations")
    order: Mapped["Order"] = relationship(back_populates="product_associations")


class InvoiceProductAssociation(ItemsMixin, db.Model):
    __tablename__ = 'invoice_product_association'

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), primary_key=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey('invoice.id'))
    product: Mapped["Product"] = relationship(back_populates="invoice_associations")
    invoice: Mapped["Invoice"] = relationship(back_populates="product_associations")


class GoodsDeliveryNoteProductAssociation(ItemsMixin, db.Model):
    __tablename__ = 'goods_delivery_note_product_association'

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), primary_key=True)
    goods_delivery_note_id: Mapped[int] = mapped_column(ForeignKey('goods_delivery_note.id'))
    product: Mapped["Product"] = relationship(back_populates="goods_delivery_note_associations")
    goods_delivery_note: Mapped["GoodsDeliveryNote"] = relationship(back_populates="product_associations")


class TaxInvoiceProductAssociation(ItemsMixin, db.Model):
    __tablename__ = 'tax_invoice_product_association'

    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), primary_key=True)
    tax_invoice_id: Mapped[int] = mapped_column(ForeignKey('tax_invoice.id'))
    product: Mapped["Product"] = relationship(back_populates="tax_invoice_associations")
    tax_invoice: Mapped["GoodsDeliveryNote"] = relationship(back_populates="product_associations")


