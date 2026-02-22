from flaskr.directory.schemas import (
    OperationTypeCreateSchema,
    OperationTypeUpdateSchema,
    OperationTypeResponseSchema,
    OperationTypeListSchema,
)
from flaskr.directory.services import OperationTypeService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'OperationTypeDetailAPI',
    'OperationTypeListAPI',
    'OperationTypeCreateAPI',
    'OperationTypeUpdateAPI',
    'OperationTypeDeleteAPI',
)


class OperationTypeListAPI(ListAPI):
    service = OperationTypeService
    request_schema = OperationTypeListSchema
    response_schema = OperationTypeResponseSchema


class OperationTypeDetailAPI(DetailAPI):
    service = OperationTypeService
    response_schema = OperationTypeResponseSchema


class OperationTypeCreateAPI(CreateAPI):
    service = OperationTypeService
    request_schema = OperationTypeCreateSchema
    response_schema = OperationTypeResponseSchema


class OperationTypeUpdateAPI(UpdateAPI):
    service = OperationTypeService
    request_schema = OperationTypeUpdateSchema
    response_schema = OperationTypeResponseSchema


class OperationTypeDeleteAPI(DeleteAPI):
    service = OperationTypeService
