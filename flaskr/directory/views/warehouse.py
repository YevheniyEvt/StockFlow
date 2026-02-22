from flask import request
from flask.views import MethodView

from flaskr.directory.schemas import (
    WarehouseCreateSchema,
    WarehouseUpdateSchema,
    WarehouseResponseSchema,
    WarehouseListSchema,
)
from flaskr.directory.services import WarehouseService

__all__ = (
    'WarehouseDetailAPI',
    'WarehouseListAPI',
    'WarehouseCreateAPI',
    'WarehouseUpdateAPI',
    'WarehouseDeleteAPI',
)


class WarehouseListAPI(MethodView):

    def get(self):
        data = WarehouseListSchema.model_validate(request.json)
        items = WarehouseService.all(data)
        return [WarehouseResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class WarehouseDetailAPI(MethodView):

    def get(self, id):
        warehouse = WarehouseService.get_or_404(id)
        return WarehouseResponseSchema.model_validate(warehouse).model_dump(mode='json')


class WarehouseCreateAPI(MethodView):

    def post(self):
        data = WarehouseCreateSchema.model_validate(request.json)
        warehouse = WarehouseService.create(data)
        return WarehouseResponseSchema.model_validate(warehouse).model_dump(mode='json'), 201


class WarehouseUpdateAPI(MethodView):

    def patch(self, id):
        warehouse = WarehouseService.get_or_404(id)
        data = WarehouseUpdateSchema.model_validate(request.json)
        warehouse_update = WarehouseService.update(warehouse, data)
        return WarehouseResponseSchema.model_validate(warehouse_update).model_dump(mode='json')


class WarehouseDeleteAPI(MethodView):

    def delete(self, id):
        warehouse = WarehouseService.get_or_404(id)
        WarehouseService.delete(warehouse)
        return '', 204