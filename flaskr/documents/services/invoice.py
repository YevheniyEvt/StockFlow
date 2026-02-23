from flaskr import db, Order
from flaskr.core.services import BaseService
from flaskr.documents.models import Invoice
from flaskr.documents.models.document_enum import OrderStatus
from flaskr.documents.services.mixin import DocumentsAllMixin, CreateDocumentItemMixin

__all__ = (
    'InvoiceService',
)


class InvoiceService(DocumentsAllMixin, CreateDocumentItemMixin, BaseService[Invoice]):
    model = Invoice

    @classmethod
    def create(cls, data):
        invoice = super().create(data)
        invoice_id = invoice.id
        order = invoice.order
        order.status = OrderStatus.CONFIRMED_BY_CLIENT
        db.session.add(order)
        db.session.commit()
        for item in order.items:
            cls._create_document_item(item, invoice_id)
        return invoice