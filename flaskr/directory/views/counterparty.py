from flaskr.directory.schemas import (
    CounterpartyCreateSchema,
    CounterpartyUpdateSchema,
    CounterpartyResponseSchema,
    CounterpartyListSchema,
)
from flaskr.directory.services import CounterpartyService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'CounterpartyDetailAPI',
    'CounterpartyListAPI',
    'CounterpartyCreateAPI',
    'CounterpartyUpdateAPI',
    'CounterpartyDeleteAPI',
)


class CounterpartyListAPI(ListAPI):
    service = CounterpartyService
    request_schema = CounterpartyListSchema
    response_schema = CounterpartyResponseSchema


class CounterpartyDetailAPI(DetailAPI):
    service = CounterpartyService
    response_schema = CounterpartyResponseSchema


class CounterpartyCreateAPI(CreateAPI):
    service = CounterpartyService
    request_schema = CounterpartyCreateSchema
    response_schema = CounterpartyResponseSchema


class CounterpartyUpdateAPI(UpdateAPI):
    service = CounterpartyService
    request_schema = CounterpartyUpdateSchema
    response_schema = CounterpartyResponseSchema


class CounterpartyDeleteAPI(DeleteAPI):
    service = CounterpartyService
