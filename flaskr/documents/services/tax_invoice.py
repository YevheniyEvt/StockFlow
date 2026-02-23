from flaskr import db
from flaskr.core.services import BaseService
from flaskr.documents.models import TaxInvoice
from flaskr.documents.services.mixin import DocumentsAllMixin, CreateDocumentItemMixin

__all__ = (
    'TaxInvoiceService',
)


class TaxInvoiceService(DocumentsAllMixin, CreateDocumentItemMixin, BaseService[TaxInvoice]):
    model = TaxInvoice

    @classmethod
    def create(cls, data):
        tax_invoice = super().create(data, commit=False)
        for item in tax_invoice.goods_delivery_note.items:
            cls._create_document_item(item, tax_invoice.id)
        db.session.commit()
        db.session.refresh(tax_invoice)
        return tax_invoice