from typing import List

from sqlalchemy import select

from flaskr import db, Document, Order, Invoice
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    GoodsDeliveryNote,
)

__all__ = (
    'GoodsDeliveryNoteService',
)

from flaskr.documents.services.mixin import DocumentsAllMixin, CreateDocumentItemMixin


class GoodsDeliveryNoteService(DocumentsAllMixin, CreateDocumentItemMixin, BaseService[GoodsDeliveryNote]):
    model = GoodsDeliveryNote

    @classmethod
    def create(cls, data):
        goods_delivery_note = super().create(data)
        goods_delivery_note_id = goods_delivery_note.id
        invoice = goods_delivery_note.invoice
        for item in invoice.items:
            cls._create_document_item(item, goods_delivery_note_id)
        return goods_delivery_note
