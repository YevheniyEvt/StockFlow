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
        invoice = super().create(data, commit=False)
        order = invoice.order
        order.status = OrderStatus.CONFIRMED_BY_CLIENT
        for item in order.items:
            cls._create_document_item(item, invoice.id)
        db.session.commit()
        db.session.refresh(invoice)
        return invoice