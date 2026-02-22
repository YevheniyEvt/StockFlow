from flaskr.core.services import BaseService
from flaskr.documents.models import TaxInvoice
from flaskr.documents.services.mixin import DocumentsAllMixin

__all__ = (
    'TaxInvoiceService',
)


class TaxInvoiceService(DocumentsAllMixin, BaseService[TaxInvoice]):
    model = TaxInvoice