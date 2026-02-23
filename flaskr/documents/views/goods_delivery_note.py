from flask import request, jsonify
from flaskr.documents.schemas import (
    GoodsDeliveryNoteUpdateSchema,
    GoodsDeliveryNoteResponseSchema,
    GoodsDeliveryNoteListSchema,
    GoodsDeliveryNoteChangeStatusSchema,
    GoodsDeliveryNoteCreateSchema,
)
from flaskr.documents.services import GoodsDeliveryNoteService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'GoodsDeliveryNoteDetailAPI',
    'GoodsDeliveryNoteListAPI',
    'GoodsDeliveryNoteUpdateAPI',
    'GoodsDeliveryNoteDeleteAPI',
    'GoodsDeliveryNoteChangeStatusAPI',
    'GoodsDeliveryNoteCreateAPI',
)


class GoodsDeliveryNoteListAPI(ListAPI):
    service = GoodsDeliveryNoteService
    request_schema = GoodsDeliveryNoteListSchema
    response_schema = GoodsDeliveryNoteResponseSchema


class GoodsDeliveryNoteDetailAPI(DetailAPI):
    service = GoodsDeliveryNoteService
    response_schema = GoodsDeliveryNoteResponseSchema


class GoodsDeliveryNoteCreateAPI(CreateAPI):
    service = GoodsDeliveryNoteService
    request_schema = GoodsDeliveryNoteCreateSchema
    response_schema = GoodsDeliveryNoteResponseSchema


class GoodsDeliveryNoteUpdateAPI(UpdateAPI):
    service = GoodsDeliveryNoteService
    request_schema = GoodsDeliveryNoteUpdateSchema
    response_schema = GoodsDeliveryNoteResponseSchema


class GoodsDeliveryNoteDeleteAPI(DeleteAPI):
    service = GoodsDeliveryNoteService


class GoodsDeliveryNoteChangeStatusAPI(UpdateAPI):
    service = GoodsDeliveryNoteService
    request_schema = GoodsDeliveryNoteChangeStatusSchema
    response_schema = GoodsDeliveryNoteResponseSchema

    def patch(self, id):
        payload = request.get_json(silent=False)
        data = self.validate(payload)
        try:
            updated_instance = self.service.change_status(id, data.status.value)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        return self.serialize(updated_instance)