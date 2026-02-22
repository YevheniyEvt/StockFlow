from typing import List

from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    TaxInvoice,
)

__all__ = (
    'TaxInvoiceService',
)


class TaxInvoiceService(BaseService[TaxInvoice]):
    model = TaxInvoice

    @staticmethod
    def change_status(tax_invoice, data):
        tax_invoice.update_from_json(data)
        db.session.commit()
        db.session.refresh(tax_invoice)
        return tax_invoice