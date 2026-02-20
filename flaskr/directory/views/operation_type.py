from flask import request
from flask.views import MethodView

from flaskr.directory.schemas import (
    OperationTypeCreateSchema,
    OperationTypeUpdateSchema,
    OperationTypeResponseSchema
)
from flaskr.directory.schemas.operation_type import OperationTypeListSchema
from flaskr.directory.services import OperationTypeService

__all__ = (
    'OperationTypeDetailAPI',
    'OperationTypeListAPI',
    'OperationTypeCreateAPI',
    'OperationTypeUpdateAPI',
    'OperationTypeDeleteAPI',
)


class OperationTypeListAPI(MethodView):

    def get(self):
        data = OperationTypeListSchema.model_validate(request.json)
        items = OperationTypeService.all(data)
        return [OperationTypeResponseSchema.model_validate(item).model_dump() for item in items]


class OperationTypeDetailAPI(MethodView):

    def get(self, id):
        organization = OperationTypeService.get_or_404(id)
        return OperationTypeResponseSchema.model_validate(organization).model_dump()


class OperationTypeCreateAPI(MethodView):

    def post(self):
        data = OperationTypeCreateSchema.model_validate(request.json)
        organization = OperationTypeService.create(data)
        return OperationTypeResponseSchema.model_validate(organization).model_dump(), 201


class OperationTypeUpdateAPI(MethodView):

    def patch(self, id):
        organization = OperationTypeService.get_or_404(id)
        data = OperationTypeUpdateSchema.model_validate(request.json)
        organization_update = OperationTypeService.update(organization, data)
        return OperationTypeResponseSchema.model_validate(organization_update).model_dump()


class OperationTypeDeleteAPI(MethodView):

    def delete(self, id):
        organization = OperationTypeService.get_or_404(id)
        OperationTypeService.delete(organization)
        return '', 204