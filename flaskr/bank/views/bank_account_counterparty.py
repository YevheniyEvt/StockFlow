from flask import request
from flask.views import MethodView

from flaskr.bank.schemas import (
    BankAccountCounterpartyUpdateSchema,
    BankAccountCounterpartyResponseSchema,
    BankAccountCounterpartyListSchema,
    BankAccountCounterpartyCreateSchema,
)
from flaskr.bank.services import BankAccountCounterpartyService

__all__ = (
    'BankAccountCounterpartyDetailAPI',
    'BankAccountCounterpartyListAPI',
    'BankAccountCounterpartyUpdateAPI',
    'BankAccountCounterpartyDeleteAPI',
    'BankAccountCounterpartyCreateAPI',
)


class BankAccountCounterpartyListAPI(MethodView):

    def get(self):
        data = BankAccountCounterpartyListSchema.model_validate(request.json)
        items = BankAccountCounterpartyService.all(data)
        return [BankAccountCounterpartyResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class BankAccountCounterpartyDetailAPI(MethodView):

    def get(self, id):
        bank_account_counterparty = BankAccountCounterpartyService.get_or_404(id)
        return BankAccountCounterpartyResponseSchema.model_validate(bank_account_counterparty).model_dump(mode='json')


class BankAccountCounterpartyCreateAPI(MethodView):

    def post(self):
        data = BankAccountCounterpartyCreateSchema.model_validate(request.json)
        bank_account_counterparty = BankAccountCounterpartyService.create(data)
        return BankAccountCounterpartyResponseSchema.model_validate(bank_account_counterparty).model_dump(mode='json'), 201


class BankAccountCounterpartyUpdateAPI(MethodView):

    def patch(self, id):
        bank_account_counterparty = BankAccountCounterpartyService.get_or_404(id)
        data = BankAccountCounterpartyUpdateSchema.model_validate(request.json)
        bank_account_counterparty_update = BankAccountCounterpartyService.update(bank_account_counterparty, data)
        return BankAccountCounterpartyResponseSchema.model_validate(bank_account_counterparty_update).model_dump(mode='json')


class BankAccountCounterpartyDeleteAPI(MethodView):

    def delete(self, id):
        bank_account_counterparty = BankAccountCounterpartyService.get_or_404(id)
        BankAccountCounterpartyService.delete(bank_account_counterparty)
        return '', 204
