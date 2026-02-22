from flask import request
from flask.views import MethodView

from flaskr.documents.schemas import (
    GoodsDeliveryNoteUpdateSchema,
    GoodsDeliveryNoteResponseSchema,
    GoodsDeliveryNoteListSchema,
    GoodsDeliveryNoteChangeStatusSchema,
    GoodsDeliveryNoteCreateSchema,
)
from flaskr.documents.services import GoodsDeliveryNoteService

__all__ = (
    'GoodsDeliveryNoteDetailAPI',
    'GoodsDeliveryNoteListAPI',
    'GoodsDeliveryNoteUpdateAPI',
    'GoodsDeliveryNoteDeleteAPI',
    'GoodsDeliveryNoteChangeStatusAPI',
    'GoodsDeliveryNoteCreateAPI',
)


class GoodsDeliveryNoteListAPI(MethodView):

    def get(self):
        data = GoodsDeliveryNoteListSchema.model_validate(request.json)
        items = GoodsDeliveryNoteService.all(data)
        return [GoodsDeliveryNoteResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class GoodsDeliveryNoteDetailAPI(MethodView):

    def get(self, id):
        goods_delivery_note = GoodsDeliveryNoteService.get_or_404(id)
        return GoodsDeliveryNoteResponseSchema.model_validate(goods_delivery_note).model_dump(mode='json')


class GoodsDeliveryNoteCreateAPI(MethodView):

    def post(self):
        data = GoodsDeliveryNoteCreateSchema.model_validate(request.json)
        goods_delivery_note = GoodsDeliveryNoteService.create(data)
        return GoodsDeliveryNoteResponseSchema.model_validate(goods_delivery_note).model_dump(mode='json'), 201


class GoodsDeliveryNoteUpdateAPI(MethodView):

    def patch(self, id):
        goods_delivery_note = GoodsDeliveryNoteService.get_or_404(id)
        data = GoodsDeliveryNoteUpdateSchema.model_validate(request.json)
        goods_delivery_note_update = GoodsDeliveryNoteService.update(goods_delivery_note, data)
        return GoodsDeliveryNoteResponseSchema.model_validate(goods_delivery_note_update).model_dump(mode='json')


class GoodsDeliveryNoteDeleteAPI(MethodView):

    def delete(self, id):
        goods_delivery_note = GoodsDeliveryNoteService.get_or_404(id)
        GoodsDeliveryNoteService.delete(goods_delivery_note)
        return '', 204


class GoodsDeliveryNoteChangeStatusAPI(MethodView):

    def patch(self, id):
        goods_delivery_note = GoodsDeliveryNoteService.get_or_404(id)
        data = GoodsDeliveryNoteChangeStatusSchema.model_validate(request.json)
        goods_delivery_note_update = GoodsDeliveryNoteService.change_status(goods_delivery_note, data)
        return GoodsDeliveryNoteResponseSchema.model_validate(goods_delivery_note_update).model_dump(mode='json')