from flask import request
from flask.views import MethodView

from flaskr.directory.schemas import (
    UnitsOfMeasurementCreateSchema,
    UnitsOfMeasurementUpdateSchema,
    UnitsOfMeasurementResponseSchema
)
from flaskr.directory.schemas.units_of_measurement import UnitsOfMeasurementListSchema
from flaskr.directory.services import UnitsOfMeasurementService

__all__ = (
    'UnitsOfMeasurementDetailAPI',
    'UnitsOfMeasurementListAPI',
    'UnitsOfMeasurementCreateAPI',
    'UnitsOfMeasurementUpdateAPI',
    'UnitsOfMeasurementDeleteAPI',
)


class UnitsOfMeasurementListAPI(MethodView):

    def get(self):
        data = UnitsOfMeasurementListSchema.model_validate(request.json)
        items = UnitsOfMeasurementService.all(data)
        return [UnitsOfMeasurementResponseSchema.model_validate(item).model_dump() for item in items]


class UnitsOfMeasurementDetailAPI(MethodView):

    def get(self, id):
        organization = UnitsOfMeasurementService.get_or_404(id)
        return UnitsOfMeasurementResponseSchema.model_validate(organization).model_dump()


class UnitsOfMeasurementCreateAPI(MethodView):

    def post(self):
        data = UnitsOfMeasurementCreateSchema.model_validate(request.json)
        organization = UnitsOfMeasurementService.create(data)
        return UnitsOfMeasurementResponseSchema.model_validate(organization).model_dump(), 201


class UnitsOfMeasurementUpdateAPI(MethodView):

    def patch(self, id):
        organization = UnitsOfMeasurementService.get_or_404(id)
        data = UnitsOfMeasurementUpdateSchema.model_validate(request.json)
        organization_update = UnitsOfMeasurementService.update(organization, data)
        return UnitsOfMeasurementResponseSchema.model_validate(organization_update).model_dump()


class UnitsOfMeasurementDeleteAPI(MethodView):

    def delete(self, id):
        organization = UnitsOfMeasurementService.get_or_404(id)
        UnitsOfMeasurementService.delete(organization)
        return '', 204