from flask import request
from flask.views import MethodView

from flaskr.nomenclature.schemas import (
    ServiceCreateSchema,
    ServiceUpdateSchema,
    ServiceResponseSchema
)
from flaskr.nomenclature.schemas import ServiceListSchema
from flaskr.nomenclature.services import ServiceService

__all__ = (
    'ServiceDetailAPI',
    'ServiceListAPI',
    'ServiceCreateAPI',
    'ServiceUpdateAPI',
    'ServiceDeleteAPI',
)


class ServiceListAPI(MethodView):

    def get(self):
        data = ServiceListSchema.model_validate(request.json)
        items = ServiceService.all(data)
        return [ServiceResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class ServiceDetailAPI(MethodView):

    def get(self, id):
        service = ServiceService.get_or_404(id)
        return ServiceResponseSchema.model_validate(service).model_dump(mode='json')


class ServiceCreateAPI(MethodView):

    def post(self):
        data = ServiceCreateSchema.model_validate(request.json)
        service = ServiceService.create(data)
        return ServiceResponseSchema.model_validate(service).model_dump(mode='json'), 201


class ServiceUpdateAPI(MethodView):

    def patch(self, id):
        service = ServiceService.get_or_404(id)
        data = ServiceUpdateSchema.model_validate(request.json)
        service_update = ServiceService.update(service, data)
        return ServiceResponseSchema.model_validate(service_update).model_dump(mode='json')


class ServiceDeleteAPI(MethodView):

    def delete(self, id):
        service = ServiceService.get_or_404(id)
        ServiceService.delete(service)
        return '', 204