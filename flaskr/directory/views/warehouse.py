from flask import request
from flask.views import MethodView

from flaskr.directory.schemas import (
    WarehouseCreateSchema,
    WarehouseUpdateSchema,
    WarehouseResponseSchema
)
from flaskr.directory.schemas.warehouse import WarehouseListSchema
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
        return [WarehouseResponseSchema.model_validate(item).model_dump() for item in items]


class WarehouseDetailAPI(MethodView):

    def get(self, id):
        organization = WarehouseService.get_or_404(id)
        return WarehouseResponseSchema.model_validate(organization).model_dump()


class WarehouseCreateAPI(MethodView):

    def post(self):
        data = WarehouseCreateSchema.model_validate(request.json)
        organization = WarehouseService.create(data)
        return WarehouseResponseSchema.model_validate(organization).model_dump(), 201


class WarehouseUpdateAPI(MethodView):

    def patch(self, id):
        organization = WarehouseService.get_or_404(id)
        data = WarehouseUpdateSchema.model_validate(request.json)
        organization_update = WarehouseService.update(organization, data)
        return WarehouseResponseSchema.model_validate(organization_update).model_dump()


class WarehouseDeleteAPI(MethodView):

    def delete(self, id):
        organization = WarehouseService.get_or_404(id)
        WarehouseService.delete(organization)
        return '', 204