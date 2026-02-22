from flaskr.documents.schemas import (
    GoodsReceivedNoteUpdateSchema,
    GoodsReceivedNoteResponseSchema,
    GoodsReceivedNoteListSchema,
    GoodsReceivedNoteChangeStatusSchema,
    GoodsReceivedNoteCreateSchema,
)
from flaskr.documents.services import GoodsReceivedNoteService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'GoodsReceivedNoteDetailAPI',
    'GoodsReceivedNoteListAPI',
    'GoodsReceivedNoteUpdateAPI',
    'GoodsReceivedNoteDeleteAPI',
    'GoodsReceivedNoteChangeStatusAPI',
    'GoodsReceivedNoteCreateAPI',
)


class GoodsReceivedNoteListAPI(ListAPI):
    service = GoodsReceivedNoteService
    request_schema = GoodsReceivedNoteListSchema
    response_schema = GoodsReceivedNoteResponseSchema


class GoodsReceivedNoteDetailAPI(DetailAPI):
    service = GoodsReceivedNoteService
    response_schema = GoodsReceivedNoteResponseSchema


class GoodsReceivedNoteCreateAPI(CreateAPI):
    service = GoodsReceivedNoteService
    request_schema = GoodsReceivedNoteCreateSchema
    response_schema = GoodsReceivedNoteResponseSchema
    
    
class GoodsReceivedNoteUpdateAPI(UpdateAPI):
    service = GoodsReceivedNoteService
    request_schema = GoodsReceivedNoteUpdateSchema
    response_schema = GoodsReceivedNoteResponseSchema


class GoodsReceivedNoteDeleteAPI(DeleteAPI):
    service = GoodsReceivedNoteService


class GoodsReceivedNoteChangeStatusAPI(UpdateAPI):
    service = GoodsReceivedNoteService
    request_schema = GoodsReceivedNoteChangeStatusSchema
    response_schema = GoodsReceivedNoteResponseSchema