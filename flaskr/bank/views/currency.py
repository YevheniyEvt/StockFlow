from flask import request
from flask.views import MethodView

from flaskr.bank.schemas import (
    CurrencyUpdateSchema,
    CurrencyResponseSchema,
    CurrencyListSchema,
    CurrencyCreateSchema,
)
from flaskr.bank.services import CurrencyService

__all__ = (
    'CurrencyDetailAPI',
    'CurrencyListAPI',
    'CurrencyUpdateAPI',
    'CurrencyDeleteAPI',
    'CurrencyCreateAPI',
)


class CurrencyListAPI(MethodView):

    def get(self):
        data = CurrencyListSchema.model_validate(request.json)
        items = CurrencyService.all(data)
        return [CurrencyResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class CurrencyDetailAPI(MethodView):

    def get(self, id):
        currency = CurrencyService.get_or_404(id)
        return CurrencyResponseSchema.model_validate(currency).model_dump(mode='json')


class CurrencyCreateAPI(MethodView):

    def post(self):
        data = CurrencyCreateSchema.model_validate(request.json)
        currency = CurrencyService.create(data)
        return CurrencyResponseSchema.model_validate(currency).model_dump(mode='json'), 201


class CurrencyUpdateAPI(MethodView):

    def patch(self, id):
        currency = CurrencyService.get_or_404(id)
        data = CurrencyUpdateSchema.model_validate(request.json)
        currency_update = CurrencyService.update(currency, data)
        return CurrencyResponseSchema.model_validate(currency_update).model_dump(mode='json')


class CurrencyDeleteAPI(MethodView):

    def delete(self, id):
        currency = CurrencyService.get_or_404(id)
        CurrencyService.delete(currency)
        return '', 204
