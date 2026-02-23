from flask import request
from flask.views import MethodView

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


class HeldGodsReceivedNote(MethodView):
    service = GoodsReceivedNoteService
    response_schema = GoodsReceivedNoteResponseSchema

    def post(self, id):
        goods_received_note = self.service.get_or_404(id)
        payload = request.get_json(silent=False)
        self.service.held(goods_received_note, payload)
        return self.response_schema.model_validate(goods_received_note).model_dump(mode='json')