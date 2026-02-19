from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from flaskr import db
from flaskr.models.mixins import ItemsMixin


__all__ = (
    'GoodsReceivedNoteServiceAssociation',
    'OrderServiceAssociation',
    'InvoiceServiceAssociation',
    'GoodsDeliveryNoteServiceAssociation',
    'TaxInvoiceServiceAssociation',
)


class GoodsReceivedNoteServiceAssociation(ItemsMixin, db.Model):
    __tablename__ = 'goods_received_note_Service_association'

    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'), primary_key=True, nullable=True)
    goods_received_note_id: Mapped[int] = mapped_column(ForeignKey('goods_received_note.id'), primary_key=True)
    service: Mapped["Service"] = relationship(back_populates="goods_received_note_associations")
    goods_received_note: Mapped["GoodsReceivedNote"] = relationship(back_populates="Service_associations")


class OrderServiceAssociation(ItemsMixin, db.Model):
    __tablename__ = 'order_Service_association'

    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'), primary_key=True, nullable=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('order.id'))
    service: Mapped["Service"] = relationship(back_populates="order_associations")
    order: Mapped["Order"] = relationship(back_populates="service_associations")


class InvoiceServiceAssociation(ItemsMixin, db.Model):
    __tablename__ = 'invoice_items'

    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'), primary_key=True, nullable=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey('invoice.id'))
    service: Mapped["Service"] = relationship(back_populates="invoice_associations")
    invoice: Mapped["Invoice"] = relationship(back_populates="service_associations")


class GoodsDeliveryNoteServiceAssociation(ItemsMixin, db.Model):
    __tablename__ = 'goods_delivery_note_Service_association'

    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'), primary_key=True, nullable=True)
    goods_delivery_note_id: Mapped[int] = mapped_column(ForeignKey('goods_delivery_note.id'))
    service: Mapped["Service"] = relationship(back_populates="goods_delivery_note_associations")
    goods_delivery_note: Mapped["GoodsDeliveryNote"] = relationship(back_populates="service_associations")


class TaxInvoiceServiceAssociation(ItemsMixin, db.Model):
    __tablename__ = 'tax_invoice_Service_association'

    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'), primary_key=True, nullable=True)
    tax_invoice_id: Mapped[int] = mapped_column(ForeignKey('tax_invoice.id'))
    service: Mapped["Service"] = relationship(back_populates="tax_invoice_associations")
    tax_invoice: Mapped["GoodsDeliveryNote"] = relationship(back_populates="Service_associations")


