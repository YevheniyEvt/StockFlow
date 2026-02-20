from flask import request
from flask.views import MethodView

from flaskr.directory.schemas import (
    CounterpartyCreateSchema,
    CounterpartyUpdateSchema,
    CounterpartyResponseSchema
)
from flaskr.directory.schemas.counterparty import CounterpartyListSchema
from flaskr.directory.services import CounterpartyService

__all__ = (
    'CounterpartyDetailAPI',
    'CounterpartyListAPI',
    'CounterpartyCreateAPI',
    'CounterpartyUpdateAPI',
    'CounterpartyDeleteAPI',
)


class CounterpartyListAPI(MethodView):

    def get(self):
        data = CounterpartyListSchema.model_validate(request.json)
        items = CounterpartyService.all(data)
        return [CounterpartyResponseSchema.model_validate(item).model_dump() for item in items]


class CounterpartyDetailAPI(MethodView):

    def get(self, id):
        organization = CounterpartyService.get_or_404(id)
        return CounterpartyResponseSchema.model_validate(organization).model_dump()


class CounterpartyCreateAPI(MethodView):

    def post(self):
        data = CounterpartyCreateSchema.model_validate(request.json)
        organization = CounterpartyService.create(data)
        return CounterpartyResponseSchema.model_validate(organization).model_dump(), 201


class CounterpartyUpdateAPI(MethodView):

    def patch(self, id):
        organization = CounterpartyService.get_or_404(id)
        data = CounterpartyUpdateSchema.model_validate(request.json)
        organization_update = CounterpartyService.update(organization, data)
        return CounterpartyResponseSchema.model_validate(organization_update).model_dump()


class CounterpartyDeleteAPI(MethodView):

    def delete(self, id):
        organization = CounterpartyService.get_or_404(id)
        CounterpartyService.delete(organization)
        return '', 204