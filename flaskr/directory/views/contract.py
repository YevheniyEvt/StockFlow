from flaskr.directory.schemas import (
    ContractCreateSchema,
    ContractUpdateSchema,
    ContractResponseSchema,
    ContractListSchema,
)
from flaskr.directory.services import ContractService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'ContractDetailAPI',
    'ContractListAPI',
    'ContractCreateAPI',
    'ContractUpdateAPI',
    'ContractDeleteAPI',
)


class ContractListAPI(ListAPI):
    service = ContractService
    request_schema = ContractListSchema
    response_schema = ContractResponseSchema


class ContractDetailAPI(DetailAPI):
    service = ContractService
    response_schema = ContractResponseSchema


class ContractCreateAPI(CreateAPI):
    service = ContractService
    request_schema = ContractCreateSchema
    response_schema = ContractResponseSchema


class ContractUpdateAPI(UpdateAPI):
    service = ContractService
    request_schema = ContractUpdateSchema
    response_schema = ContractResponseSchema


class ContractDeleteAPI(DeleteAPI):
    service = ContractService