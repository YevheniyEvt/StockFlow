from flaskr.core.services import BaseService
from flaskr.documents.models import Order
from flaskr.documents.services.mixin import DocumentsAllMixin

__all__ = (
    'OrderService',
)


class OrderService(DocumentsAllMixin, BaseService[Order]):
    model = Order