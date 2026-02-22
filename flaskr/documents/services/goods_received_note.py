from typing import List

from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    GoodsReceivedNote,
)

__all__ = (
    'GoodsReceivedNoteService',
)


class GoodsReceivedNoteService(BaseService[GoodsReceivedNote]):
    model = GoodsReceivedNote

    @staticmethod
    def change_status(goods_received_note, data):
        goods_received_note.update_from_json(data)
        db.session.commit()
        db.session.refresh(goods_received_note)
        return goods_received_note