from typing import List

from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    Order,
)

__all__ = (
    'OrderService',
)


class OrderService(BaseService[Order]):
    model = Order

    @staticmethod
    def change_status(order, data):
        order.update_from_json(data)
        db.session.commit()
        db.session.refresh(order)
        return order