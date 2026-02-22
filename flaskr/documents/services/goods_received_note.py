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