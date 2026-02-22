from typing import List

from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    GoodsDeliveryNote,
)

__all__ = (
    'GoodsDeliveryNoteService',
)


class GoodsDeliveryNoteService(BaseService[GoodsDeliveryNote]):
    model = GoodsDeliveryNote

    @staticmethod
    def change_status(goods_delivery_note, data):
        goods_delivery_note.update_from_json(data)
        db.session.commit()
        db.session.refresh(goods_delivery_note)
        return goods_delivery_note