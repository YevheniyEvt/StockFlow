from flask import request
from flask.views import MethodView

from flaskr.bank.schemas import (
    BankAccountCompanyUpdateSchema,
    BankAccountCompanyResponseSchema,
    BankAccountCompanyListSchema,
    BankAccountCompanyCreateSchema,
)
from flaskr.bank.services import BankAccountCompanyService

__all__ = (
    'BankAccountCompanyDetailAPI',
    'BankAccountCompanyListAPI',
    'BankAccountCompanyUpdateAPI',
    'BankAccountCompanyDeleteAPI',
    'BankAccountCompanyCreateAPI',
)


class BankAccountCompanyListAPI(MethodView):

    def get(self):
        data = BankAccountCompanyListSchema.model_validate(request.json)
        items = BankAccountCompanyService.all(data)
        return [BankAccountCompanyResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class BankAccountCompanyDetailAPI(MethodView):

    def get(self, id):
        bank_account_company = BankAccountCompanyService.get_or_404(id)
        return BankAccountCompanyResponseSchema.model_validate(bank_account_company).model_dump(mode='json')


class BankAccountCompanyCreateAPI(MethodView):

    def post(self):
        data = BankAccountCompanyCreateSchema.model_validate(request.json)
        bank_account_company = BankAccountCompanyService.create(data)
        return BankAccountCompanyResponseSchema.model_validate(bank_account_company).model_dump(mode='json'), 201


class BankAccountCompanyUpdateAPI(MethodView):

    def patch(self, id):
        bank_account_company = BankAccountCompanyService.get_or_404(id)
        data = BankAccountCompanyUpdateSchema.model_validate(request.json)
        bank_account_company_update = BankAccountCompanyService.update(bank_account_company, data)
        return BankAccountCompanyResponseSchema.model_validate(bank_account_company_update).model_dump(mode='json')


class BankAccountCompanyDeleteAPI(MethodView):

    def delete(self, id):
        bank_account_company = BankAccountCompanyService.get_or_404(id)
        BankAccountCompanyService.delete(bank_account_company)
        return '', 204
