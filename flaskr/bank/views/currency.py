from flaskr.bank.schemas import (
    CurrencyUpdateSchema,
    CurrencyResponseSchema,
    CurrencyListSchema,
    CurrencyCreateSchema,
)
from flaskr.bank.services import CurrencyService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'CurrencyDetailAPI',
    'CurrencyListAPI',
    'CurrencyUpdateAPI',
    'CurrencyDeleteAPI',
    'CurrencyCreateAPI',
)


class CurrencyListAPI(ListAPI):
    service = CurrencyService
    request_schema = CurrencyListSchema
    response_schema = CurrencyResponseSchema


class CurrencyDetailAPI(DetailAPI):
    service = CurrencyService
    response_schema = CurrencyResponseSchema


class CurrencyCreateAPI(CreateAPI):
    service = CurrencyService
    request_schema = CurrencyCreateSchema
    response_schema = CurrencyResponseSchema


class CurrencyUpdateAPI(UpdateAPI):
    service = CurrencyService
    request_schema = CurrencyUpdateSchema
    response_schema = CurrencyResponseSchema


class CurrencyDeleteAPI(DeleteAPI):
    service = CurrencyService
