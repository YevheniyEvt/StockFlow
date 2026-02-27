from flaskr import db
from flaskr.core.services import BaseService
from flaskr.documents.models import Order
from flaskr.documents.models.document_enum import OrderStatus
from flaskr.documents.services.mixin import DocumentsAllMixin

__all__ = (
    'OrderService',
)


class OrderService(DocumentsAllMixin, BaseService[Order]):
    model = Order

    @classmethod
    def change_status(cls, order_id: int, status: str):
        order = cls.get_or_404(order_id)
        order.status = OrderStatus(status)
        db.session.commit()
        db.session.refresh(order)
        return order