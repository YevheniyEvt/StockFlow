from flaskr import db
from flaskr.core.services import BaseService
from flaskr.documents.models import TaxInvoice
from flaskr.documents.models.document_enum import TaxInvoiceStatus
from flaskr.documents.services.mixin import DocumentsAllMixin, CreateDocumentItemMixin

__all__ = (
    'TaxInvoiceService',
)


class TaxInvoiceService(DocumentsAllMixin, CreateDocumentItemMixin, BaseService[TaxInvoice]):
    model = TaxInvoice

    @classmethod
    def create(cls, data):
        tax_invoice = super().create(data, commit=False)
        goods_delivery_note = tax_invoice.goods_delivery_note

        tax_invoice.counterparty_id = goods_delivery_note.counterparty_id
        tax_invoice.warehouse_id = goods_delivery_note.warehouse_id
        tax_invoice.operation_type_id = goods_delivery_note.operation_type_id
        tax_invoice.contract_id = goods_delivery_note.contract_id
        tax_invoice.comment = goods_delivery_note.comment
        tax_invoice.amount = goods_delivery_note.amount

        for item in goods_delivery_note.items:
            cls._create_document_item(item, tax_invoice.id)
        db.session.commit()
        db.session.refresh(tax_invoice)
        return tax_invoice

    @classmethod
    def change_status(cls, tax_invoice_id: int, status: str):
        tax_invoice = cls.get_or_404(tax_invoice_id)
        tax_invoice.status = TaxInvoiceStatus(status)
        db.session.commit()
        db.session.refresh(tax_invoice)
        return tax_invoice