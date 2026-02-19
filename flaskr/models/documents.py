import enum
from datetime import datetime
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum, ForeignKey

from flaskr import db
from flaskr.models.mixins import CreatedUpdatedDateTimeMixin

__all__ = (
    'Document',
    'GoodsReceivedNote',
    'Order',
    'Invoice',
    'GoodsDeliveryNote',
    'TaxInvoice',
)


class DocumentType(enum.Enum):
    goods_received_note = "goods_received_note"
    order = "order"
    invoice = "invoice"
    goods_delivery_note = "goods_delivery_note"
    tax_invoice = "tax_invoice"


class Document(CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'document'

    counterparty_id: Mapped[int] = mapped_column(ForeignKey('counterparty.id'))
    document_type: Mapped[DocumentType] = mapped_column(Enum(DocumentType))

    __mapper_args__ = {
        "polymorphic_on": document_type,
        "polymorphic_identity": "document",
    }


class GoodsReceivedNoteStatus(enum.Enum):
    draft = "draft"
    held = "held"
    canceled = "canceled"

class GoodsReceivedNote(Document):
    __tablename__ = 'goods_received_note'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    products: Mapped[List["Product"]] = relationship(
        back_populates="goods_received_notes",
        secondary="goods_received_note_product_association"
    )
    product_associations: Mapped[List["GoodsReceivedNoteProductAssociation"]] = relationship(
        back_populates="goods_received_note"
    )

    status: Mapped[GoodsReceivedNoteStatus] = mapped_column(Enum(GoodsReceivedNoteStatus))
    held_date: Mapped[datetime | None]

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.goods_received_note,
    }


class OrderStatus(enum.Enum):
    draft = "draft"
    confirmed_by_client = "confirmed_by_client"
    canceled = "canceled"

class Order(Document):
    __tablename__ = 'order'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    invoices: Mapped[List["Invoice"]] = relationship(back_populates="order")
    products: Mapped[List["Product"]] = relationship(back_populates="orders", secondary="order_product_association")
    product_associations: Mapped[List["OrderProductAssociation"]] = relationship(back_populates="order")

    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus, native_enum=False))

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.order,
    }


class InvoiceStatus(enum.Enum):
    draft = "draft"
    invoiced = "invoiced"
    partially_paid = "partially_paid"
    paid = "paid"
    overdue = "overdue"
    canceled = "canceled"

class Invoice(Document):
    __tablename__ = 'invoice'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('order.id'))
    order: Mapped["Order"] = relationship(back_populates="invoices")
    goods_delivery_notes: Mapped[List["GoodsDeliveryNote"]] = relationship(
        back_populates="invoice"
    )
    products: Mapped[List["Product"]] = relationship(
        back_populates="invoices",
        secondary="invoice_product_association"
    )
    product_associations: Mapped[List["InvoiceProductAssociation"]] = relationship(
        back_populates="invoice"
    )

    status: Mapped[InvoiceStatus] = mapped_column(Enum(InvoiceStatus, native_enum=False))
    payment_final_date: Mapped[datetime | None]

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.invoice,
    }


class GoodsDeliveryNoteStatus(enum.Enum):
    draft = "draft"
    sent = "sent"
    signed = "signed"
    held = "held"
    rejected = "rejected"
    refund = "refund"

class GoodsDeliveryNote(Document):
    __tablename__ = 'goods_delivery_note'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey('invoice.id'))
    invoice: Mapped["Invoice"] = relationship(back_populates="goods_delivery_notes")
    products: Mapped[List["Product"]] = relationship(
        back_populates="goods_delivery_notes",
        secondary="goods_delivery_note_product_association"
    )
    product_associations: Mapped[List["GoodsDeliveryNoteProductAssociation"]] = relationship(
        back_populates="goods_delivery_note"
    )

    tax_invoices: Mapped[List["TaxInvoice"]] = relationship(back_populates="goods_delivery_note")
    status: Mapped[GoodsDeliveryNoteStatus] = mapped_column(Enum(GoodsDeliveryNoteStatus, native_enum=False))

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.goods_delivery_note,
    }


class TaxInvoiceStatus(enum.Enum):
    registered = "registered"
    rejected = "rejected"

class TaxInvoice(Document):
    __tablename__ = 'tax_invoice'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    goods_delivery_note_id: Mapped[int] = mapped_column(ForeignKey('goods_delivery_note.id'))
    goods_delivery_note: Mapped["GoodsDeliveryNote"] = relationship(back_populates="tax_invoices")
    products: Mapped[List["Product"]] = relationship(
        back_populates="tax_invoices",
        secondary="tax_invoice_product_association"
    )
    product_associations: Mapped[List["TaxInvoiceProductAssociation"]] = relationship(
        back_populates="tax_invoice"
    )

    status: Mapped[TaxInvoiceStatus] = mapped_column(Enum(TaxInvoiceStatus, native_enum=False))

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.tax_invoice,
    }

