from flask import request
from flask.views import MethodView

from flaskr.directory.schemas import (
    CounterpartyCreateSchema,
    CounterpartyUpdateSchema,
    CounterpartyResponseSchema,
    CounterpartyListSchema,
)
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
        return [CounterpartyResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class CounterpartyDetailAPI(MethodView):

    def get(self, id):
        counterparty = CounterpartyService.get_or_404(id)
        return CounterpartyResponseSchema.model_validate(counterparty).model_dump(mode='json')


class CounterpartyCreateAPI(MethodView):

    def post(self):
        data = CounterpartyCreateSchema.model_validate(request.json)
        counterparty = CounterpartyService.create(data)
        return CounterpartyResponseSchema.model_validate(counterparty).model_dump(mode='json'), 201


class CounterpartyUpdateAPI(MethodView):

    def patch(self, id):
        counterparty = CounterpartyService.get_or_404(id)
        data = CounterpartyUpdateSchema.model_validate(request.json)
        counterparty_update = CounterpartyService.update(counterparty, data)
        return CounterpartyResponseSchema.model_validate(counterparty_update).model_dump(mode='json')


class CounterpartyDeleteAPI(MethodView):

    def delete(self, id):
        counterparty = CounterpartyService.get_or_404(id)
        CounterpartyService.delete(counterparty)
        return '', 204