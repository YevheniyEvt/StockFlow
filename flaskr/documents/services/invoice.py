from typing import List

from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    Invoice,
)

__all__ = (
    'InvoiceService',
)


class InvoiceService(BaseService[Invoice]):
    model = Invoice

    @staticmethod
    def change_status(invoice, data):
        invoice.update_from_json(data)
        db.session.commit()
        db.session.refresh(invoice)
        return invoice