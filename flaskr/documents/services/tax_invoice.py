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
        tax_invoice = super().create(data)
        tax_invoice_id = tax_invoice.id
        goods_delivery_note = tax_invoice.goods_delivery_note
        for item in goods_delivery_note.items:
            cls._create_document_item(item, tax_invoice_id)
        return tax_invoice