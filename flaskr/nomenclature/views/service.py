from flaskr.nomenclature.schemas import (
    ServiceCreateSchema,
    ServiceUpdateSchema,
    ServiceResponseSchema
)
from flaskr.nomenclature.schemas import ServiceListSchema
from flaskr.nomenclature.services import ServiceService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'ServiceDetailAPI',
    'ServiceListAPI',
    'ServiceCreateAPI',
    'ServiceUpdateAPI',
    'ServiceDeleteAPI',
)


class ServiceListAPI(ListAPI):
    service = ServiceService
    request_schema = ServiceListSchema
    response_schema = ServiceResponseSchema


class ServiceDetailAPI(DetailAPI):
    service = ServiceService
    response_schema = ServiceResponseSchema


class ServiceCreateAPI(CreateAPI):
    service = ServiceService
    request_schema = ServiceCreateSchema
    response_schema = ServiceResponseSchema


class ServiceUpdateAPI(UpdateAPI):
    service = ServiceService
    request_schema = ServiceUpdateSchema
    response_schema = ServiceResponseSchema


class ServiceDeleteAPI(DeleteAPI):
    service = ServiceService