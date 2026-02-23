from datetime import datetime

from flaskr import db
from flaskr.accounting.services import MovementService
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    GoodsReceivedNote,
)
from flaskr.documents.models.document_enum import GoodsReceivedNoteStatus
from flaskr.documents.services.mixin import DocumentsAllMixin
__all__ = (
    'GoodsReceivedNoteService',
)

class GoodsReceivedNoteService(DocumentsAllMixin, BaseService[GoodsReceivedNote]):
    model = GoodsReceivedNote

    @classmethod
    def held_note(cls, goods_received_note: GoodsReceivedNote, payload):
        goods_received_note.held_date = datetime.now()
        goods_received_note.status = GoodsReceivedNoteStatus.HELD
        db.session.add(goods_received_note)
        for item in goods_received_note.items:
            MovementService.create_purchase(item, commit=False)
        db.session.commit()
        db.session.refresh(goods_received_note)

