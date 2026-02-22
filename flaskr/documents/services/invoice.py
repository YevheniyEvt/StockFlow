from flaskr.core.services import BaseService
from flaskr.documents.models import Invoice
from flaskr.documents.services.mixin import DocumentsAllMixin


__all__ = (
    'InvoiceService',
)


class InvoiceService(DocumentsAllMixin, BaseService[Invoice]):
    model = Invoice