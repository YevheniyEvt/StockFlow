from flask import request
from flask.views import MethodView

from flaskr.directory.schemas import (
    OperationTypeCreateSchema,
    OperationTypeUpdateSchema,
    OperationTypeResponseSchema,
    OperationTypeListSchema,
)
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
        return [OperationTypeResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class OperationTypeDetailAPI(MethodView):

    def get(self, id):
        operation_type = OperationTypeService.get_or_404(id)
        return OperationTypeResponseSchema.model_validate(operation_type).model_dump(mode='json')


class OperationTypeCreateAPI(MethodView):

    def post(self):
        data = OperationTypeCreateSchema.model_validate(request.json)
        operation_type = OperationTypeService.create(data)
        return OperationTypeResponseSchema.model_validate(operation_type).model_dump(mode='json'), 201


class OperationTypeUpdateAPI(MethodView):

    def patch(self, id):
        operation_type = OperationTypeService.get_or_404(id)
        data = OperationTypeUpdateSchema.model_validate(request.json)
        operation_type_update = OperationTypeService.update(operation_type, data)
        return OperationTypeResponseSchema.model_validate(operation_type_update).model_dump(mode='json')


class OperationTypeDeleteAPI(MethodView):

    def delete(self, id):
        operation_type = OperationTypeService.get_or_404(id)
        OperationTypeService.delete(operation_type)
        return '', 204