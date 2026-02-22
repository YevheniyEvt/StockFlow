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

__all__ = (
    'GoodsReceivedNoteDetailAPI',
    'GoodsReceivedNoteListAPI',
    'GoodsReceivedNoteUpdateAPI',
    'GoodsReceivedNoteDeleteAPI',
    'GoodsReceivedNoteChangeStatusAPI',
    'GoodsReceivedNoteCreateAPI',
)


class GoodsReceivedNoteListAPI(MethodView):

    def get(self):
        data = GoodsReceivedNoteListSchema.model_validate(request.json)
        items = GoodsReceivedNoteService.all(data)
        return [GoodsReceivedNoteResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class GoodsReceivedNoteDetailAPI(MethodView):

    def get(self, id):
        goods_received_note = GoodsReceivedNoteService.get_or_404(id)
        return GoodsReceivedNoteResponseSchema.model_validate(goods_received_note).model_dump(mode='json')


class GoodsReceivedNoteCreateAPI(MethodView):

    def post(self):
        data = GoodsReceivedNoteCreateSchema.model_validate(request.json)
        goods_received_note = GoodsReceivedNoteService.create(data)
        return GoodsReceivedNoteResponseSchema.model_validate(goods_received_note).model_dump(mode='json'), 201
    
    
class GoodsReceivedNoteUpdateAPI(MethodView):

    def patch(self, id):
        goods_received_note = GoodsReceivedNoteService.get_or_404(id)
        data = GoodsReceivedNoteUpdateSchema.model_validate(request.json)
        goods_received_note_update = GoodsReceivedNoteService.update(goods_received_note, data)
        return GoodsReceivedNoteResponseSchema.model_validate(goods_received_note_update).model_dump(mode='json')


class GoodsReceivedNoteDeleteAPI(MethodView):

    def delete(self, id):
        goods_received_note = GoodsReceivedNoteService.get_or_404(id)
        GoodsReceivedNoteService.delete(goods_received_note)
        return '', 204


class GoodsReceivedNoteChangeStatusAPI(MethodView):

    def patch(self, id):
        goods_received_note = GoodsReceivedNoteService.get_or_404(id)
        data = GoodsReceivedNoteChangeStatusSchema.model_validate(request.json)
        goods_received_note_update = GoodsReceivedNoteService.change_status(goods_received_note, data)
        return GoodsReceivedNoteResponseSchema.model_validate(goods_received_note_update).model_dump(mode='json')