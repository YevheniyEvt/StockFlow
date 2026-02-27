from flaskr import db, Order
from flaskr.core.services import BaseService
from flaskr.documents.models import Invoice
from flaskr.documents.models.document_enum import OrderStatus, InvoiceStatus
from flaskr.documents.services.mixin import DocumentsAllMixin, CreateDocumentItemMixin

__all__ = (
    'InvoiceService',
)


class InvoiceService(DocumentsAllMixin, CreateDocumentItemMixin, BaseService[Invoice]):
    model = Invoice

    @classmethod
    def create(cls, data):
        invoice = super().create(data, commit=False)
        order = invoice.order
        order.status = OrderStatus.CONFIRMED_BY_CLIENT
        
        invoice.counterparty_id = order.counterparty_id
        invoice.warehouse_id = order.warehouse_id
        invoice.operation_type_id = order.operation_type_id
        invoice.contract_id = order.contract_id
        invoice.comment = order.comment
        invoice.amount = order.amount

        for item in order.items:
            cls._create_document_item(item, invoice.id)
        db.session.commit()
        db.session.refresh(invoice)
        return invoice

    @classmethod
    def change_status(cls, invoice_id: int, status: str):
        invoice = cls.get_or_404(invoice_id)
        invoice.status = InvoiceStatus(status)
        db.session.commit()
        db.session.refresh(invoice)
        return invoice