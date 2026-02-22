from typing import List

from sqlalchemy import select

from flaskr import db, Document
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    GoodsDeliveryNote,
)

__all__ = (
    'GoodsDeliveryNoteService',
)

from flaskr.documents.services.mixin import DocumentsAllMixin


class GoodsDeliveryNoteService(DocumentsAllMixin, BaseService[GoodsDeliveryNote]):
    model = GoodsDeliveryNote


