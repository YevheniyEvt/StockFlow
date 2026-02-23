from datetime import datetime

from flaskr import db
from flaskr.accounting.services import ProductMovementService
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    GoodsReceivedNote,
)
from flaskr.documents.services.mixin import DocumentsAllMixin
__all__ = (
    'GoodsReceivedNoteService',
)

class GoodsReceivedNoteService(DocumentsAllMixin, BaseService[GoodsReceivedNote]):
    model = GoodsReceivedNote

    @classmethod
    def held(cls, goods_received_note: GoodsReceivedNote, payload):
        goods_received_note.held_date = datetime.now()
        db.session.commit()
        db.session.refresh(goods_received_note)
        warehouse_id = payload.get('warehouse_id')
        for item in goods_received_note.items:
            ProductMovementService.create(item, warehouse_id)

