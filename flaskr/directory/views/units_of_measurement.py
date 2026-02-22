from flaskr.directory.schemas import (
    UnitsOfMeasurementCreateSchema,
    UnitsOfMeasurementUpdateSchema,
    UnitsOfMeasurementResponseSchema,
    UnitsOfMeasurementListSchema,
)
from flaskr.directory.services import UnitsOfMeasurementService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'UnitsOfMeasurementDetailAPI',
    'UnitsOfMeasurementListAPI',
    'UnitsOfMeasurementCreateAPI',
    'UnitsOfMeasurementUpdateAPI',
    'UnitsOfMeasurementDeleteAPI',
)


class UnitsOfMeasurementListAPI(ListAPI):
    service = UnitsOfMeasurementService
    request_schema = UnitsOfMeasurementListSchema
    response_schema = UnitsOfMeasurementResponseSchema


class UnitsOfMeasurementDetailAPI(DetailAPI):
    service = UnitsOfMeasurementService
    response_schema = UnitsOfMeasurementResponseSchema


class UnitsOfMeasurementCreateAPI(CreateAPI):
    service = UnitsOfMeasurementService
    request_schema = UnitsOfMeasurementCreateSchema
    response_schema = UnitsOfMeasurementResponseSchema


class UnitsOfMeasurementUpdateAPI(UpdateAPI):
    service = UnitsOfMeasurementService
    request_schema = UnitsOfMeasurementUpdateSchema
    response_schema = UnitsOfMeasurementResponseSchema


class UnitsOfMeasurementDeleteAPI(DeleteAPI):
    service = UnitsOfMeasurementService