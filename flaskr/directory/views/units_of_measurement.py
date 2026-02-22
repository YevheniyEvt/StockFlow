from flask import request
from flask.views import MethodView

from flaskr.directory.schemas import (
    UnitsOfMeasurementCreateSchema,
    UnitsOfMeasurementUpdateSchema,
    UnitsOfMeasurementResponseSchema,
    UnitsOfMeasurementListSchema,
)
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
        return [UnitsOfMeasurementResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class UnitsOfMeasurementDetailAPI(MethodView):

    def get(self, id):
        units_of_measurement = UnitsOfMeasurementService.get_or_404(id)
        return UnitsOfMeasurementResponseSchema.model_validate(units_of_measurement).model_dump(mode='json')


class UnitsOfMeasurementCreateAPI(MethodView):

    def post(self):
        data = UnitsOfMeasurementCreateSchema.model_validate(request.json)
        units_of_measurement = UnitsOfMeasurementService.create(data)
        return UnitsOfMeasurementResponseSchema.model_validate(units_of_measurement).model_dump(mode='json'), 201


class UnitsOfMeasurementUpdateAPI(MethodView):

    def patch(self, id):
        units_of_measurement = UnitsOfMeasurementService.get_or_404(id)
        data = UnitsOfMeasurementUpdateSchema.model_validate(request.json)
        units_of_measurement_update = UnitsOfMeasurementService.update(units_of_measurement, data)
        return UnitsOfMeasurementResponseSchema.model_validate(units_of_measurement_update).model_dump(mode='json')


class UnitsOfMeasurementDeleteAPI(MethodView):

    def delete(self, id):
        units_of_measurement = UnitsOfMeasurementService.get_or_404(id)
        UnitsOfMeasurementService.delete(units_of_measurement)
        return '', 204