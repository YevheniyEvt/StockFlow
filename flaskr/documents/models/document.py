from datetime import datetime
from decimal import Decimal
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from sqlalchemy import Enum, ForeignKey, Numeric, String, DateTime, CheckConstraint

from flaskr import db
from flaskr.core.mixins import CreatedUpdatedDateTimeMixin
from flaskr.documents.models.document_enum import (
    DocumentType,
    GoodsReceivedNoteStatus,
    OrderStatus,
    InvoiceStatus,
    GoodsDeliveryNoteStatus,
    TaxInvoiceStatus,
)

__all__ = (
    'Document',
    'GoodsReceivedNote',
    'Order',
    'Invoice',
    'GoodsDeliveryNote',
    'TaxInvoice',
)

class BaseDocument:
    operation_type_id: Mapped[int | None] = mapped_column(ForeignKey('operation_type.id'))
    contract_id: Mapped[int | None] = mapped_column(ForeignKey('contract.id'))
    warehouse_id: Mapped[int | None] = mapped_column(ForeignKey('warehouse.id'))

    amount: Mapped[Decimal | None] = mapped_column(Numeric(10,2))
    comment: Mapped[str | None] = mapped_column(String(50))
    document_date: Mapped[datetime | None] = mapped_column(DateTime, default=datetime.now)

    @declared_attr.directive
    def __table_args__(cls):
        return (
            CheckConstraint(
                "document_date >= CURRENT_TIMESTAMP",
                name=f"ck_{cls.__tablename__}_document_date_not_past",
            ),
        )


class Document(CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'document'

    organization_id: Mapped[int] = mapped_column(ForeignKey('organization.id'))
    counterparty_id: Mapped[int] = mapped_column(ForeignKey('counterparty.id'))
    document_type: Mapped[DocumentType] = mapped_column(Enum(DocumentType))

    items: Mapped[List["DocumentItem"]] = relationship("DocumentItem", back_populates="document", cascade="all, delete-orphan")

    __mapper_args__ = {
        "polymorphic_on": document_type,
    }


class GoodsReceivedNote(BaseDocument, Document):
    __tablename__ = 'goods_received_note'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    status: Mapped[GoodsReceivedNoteStatus] = mapped_column(
        Enum(GoodsReceivedNoteStatus, native_enum=False),
        default=GoodsReceivedNoteStatus.DRAFT
    )
    held_date: Mapped[datetime | None]

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.GOODS_RECEIVED_NOTE,
    }


class Order(BaseDocument, Document):
    __tablename__ = 'order'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    invoices: Mapped[List["Invoice"]] = relationship(
        back_populates="order",
        foreign_keys="Invoice.order_id"
    )
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus, native_enum=False),
        default=OrderStatus.DRAFT
    )

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.ORDER,
    }


class Invoice(BaseDocument, Document):
    __tablename__ = 'invoice'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('order.id'))
    order: Mapped["Order"] = relationship(
        back_populates="invoices",
        foreign_keys=[order_id]
    )
    goods_delivery_notes: Mapped[List["GoodsDeliveryNote"]] = relationship(
        back_populates="invoice", foreign_keys="GoodsDeliveryNote.invoice_id"
    )
    status: Mapped[InvoiceStatus] = mapped_column(
        Enum(InvoiceStatus, native_enum=False),
        default=InvoiceStatus.DRAFT
    )
    payment_final_date: Mapped[datetime | None]

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.INVOICE,
    }

    @declared_attr.directive
    def __table_args__(cls):
        return (
            CheckConstraint(
                "payment_final_date >= CURRENT_TIMESTAMP",
                name=f"ck_{cls.__tablename__}_payment_final_date_not_past",
            ),
        )


class GoodsDeliveryNote(BaseDocument, Document):
    __tablename__ = 'goods_delivery_note'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey('invoice.id'))
    invoice: Mapped["Invoice"] = relationship(
        back_populates="goods_delivery_notes",
        foreign_keys=[invoice_id],
    )
    tax_invoices: Mapped[List["TaxInvoice"]] = relationship(
        back_populates="goods_delivery_note",
        foreign_keys="TaxInvoice.goods_delivery_note_id"
    )
    status: Mapped[GoodsDeliveryNoteStatus] = mapped_column(
        Enum(GoodsDeliveryNoteStatus, native_enum=False),
        default=GoodsDeliveryNoteStatus.DRAFT
    )

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.GOODS_DELIVERY_NOTE,
    }


class TaxInvoice(BaseDocument, Document):
    __tablename__ = 'tax_invoice'

    id = mapped_column(ForeignKey("document.id"), primary_key=True)
    goods_delivery_note_id: Mapped[int] = mapped_column(ForeignKey('goods_delivery_note.id'))
    goods_delivery_note: Mapped["GoodsDeliveryNote"] = relationship(
        back_populates="tax_invoices",
        foreign_keys=[goods_delivery_note_id],
    )
    status: Mapped[TaxInvoiceStatus] = mapped_column(
        Enum(TaxInvoiceStatus, native_enum=False),
        default=TaxInvoiceStatus.DRAFT
    )

    __mapper_args__ = {
        "polymorphic_identity": DocumentType.TAX_INVOICE,
    }

