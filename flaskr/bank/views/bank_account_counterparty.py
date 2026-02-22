from flaskr.bank.schemas import (
    BankAccountCounterpartyUpdateSchema,
    BankAccountCounterpartyResponseSchema,
    BankAccountCounterpartyListSchema,
    BankAccountCounterpartyCreateSchema,
)
from flaskr.bank.services import BankAccountCounterpartyService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'BankAccountCounterpartyDetailAPI',
    'BankAccountCounterpartyListAPI',
    'BankAccountCounterpartyUpdateAPI',
    'BankAccountCounterpartyDeleteAPI',
    'BankAccountCounterpartyCreateAPI',
)


class BankAccountCounterpartyListAPI(ListAPI):
    service = BankAccountCounterpartyService
    request_schema = BankAccountCounterpartyListSchema
    response_schema = BankAccountCounterpartyResponseSchema


class BankAccountCounterpartyDetailAPI(DetailAPI):
    service = BankAccountCounterpartyService
    response_schema = BankAccountCounterpartyResponseSchema


class BankAccountCounterpartyCreateAPI(CreateAPI):
    service = BankAccountCounterpartyService
    request_schema = BankAccountCounterpartyCreateSchema
    response_schema = BankAccountCounterpartyResponseSchema


class BankAccountCounterpartyUpdateAPI(UpdateAPI):
    service = BankAccountCounterpartyService
    request_schema = BankAccountCounterpartyUpdateSchema
    response_schema = BankAccountCounterpartyResponseSchema


class BankAccountCounterpartyDeleteAPI(DeleteAPI):
    service = BankAccountCounterpartyService