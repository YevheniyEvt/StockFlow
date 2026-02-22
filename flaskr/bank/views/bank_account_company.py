from flaskr.bank.schemas import (
    BankAccountCompanyUpdateSchema,
    BankAccountCompanyResponseSchema,
    BankAccountCompanyListSchema,
    BankAccountCompanyCreateSchema,
)
from flaskr.bank.services import BankAccountCompanyService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'BankAccountCompanyDetailAPI',
    'BankAccountCompanyListAPI',
    'BankAccountCompanyUpdateAPI',
    'BankAccountCompanyDeleteAPI',
    'BankAccountCompanyCreateAPI',
)


class BankAccountCompanyListAPI(ListAPI):
    service = BankAccountCompanyService
    request_schema = BankAccountCompanyListSchema
    response_schema = BankAccountCompanyResponseSchema


class BankAccountCompanyDetailAPI(DetailAPI):
    service = BankAccountCompanyService
    response_schema = BankAccountCompanyResponseSchema


class BankAccountCompanyCreateAPI(CreateAPI):
    service = BankAccountCompanyService
    request_schema = BankAccountCompanyCreateSchema
    response_schema = BankAccountCompanyResponseSchema


class BankAccountCompanyUpdateAPI(UpdateAPI):
    service = BankAccountCompanyService
    request_schema = BankAccountCompanyUpdateSchema
    response_schema = BankAccountCompanyResponseSchema


class BankAccountCompanyDeleteAPI(DeleteAPI):
    service = BankAccountCompanyService