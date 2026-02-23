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


    #TODO При проведенні видаткової накладної при нестачі товару необхідно видавати відповідне попередження
    # із зазначенням кількості нестачі та не дозволяти проводити документ.

    #TODO Списання собівартості має бути організоване за партіями по методу FIFO.

    @classmethod
    def create(cls, data, **kwargs):
        goods_delivery_note = super().create(data, commit=False)
        for item in goods_delivery_note.invoice.items:
            cls._create_document_item(item, goods_delivery_note.id)
        db.session.commit()
        db.session.refresh(goods_delivery_note)
        return goods_delivery_note
