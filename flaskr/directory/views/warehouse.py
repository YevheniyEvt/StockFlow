from flaskr.directory.schemas import (
    WarehouseCreateSchema,
    WarehouseUpdateSchema,
    WarehouseResponseSchema,
    WarehouseListSchema,
)
from flaskr.directory.services import WarehouseService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'WarehouseDetailAPI',
    'WarehouseListAPI',
    'WarehouseCreateAPI',
    'WarehouseUpdateAPI',
    'WarehouseDeleteAPI',
)


class WarehouseListAPI(ListAPI):
    service = WarehouseService
    request_schema = WarehouseListSchema
    response_schema = WarehouseResponseSchema


class WarehouseDetailAPI(DetailAPI):
    service = WarehouseService
    response_schema = WarehouseResponseSchema


class WarehouseCreateAPI(CreateAPI):
    service = WarehouseService
    request_schema = WarehouseCreateSchema
    response_schema = WarehouseResponseSchema


class WarehouseUpdateAPI(UpdateAPI):
    service = WarehouseService
    request_schema = WarehouseUpdateSchema
    response_schema = WarehouseResponseSchema


class WarehouseDeleteAPI(DeleteAPI):
    service = WarehouseService