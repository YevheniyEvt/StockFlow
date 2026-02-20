from . import directory_bp

from flaskr.directory.views import (
    UnitsOfMeasurementDetailAPI,
    UnitsOfMeasurementListAPI,
    UnitsOfMeasurementUpdateAPI,
    UnitsOfMeasurementCreateAPI,
    UnitsOfMeasurementDeleteAPI,
)

directory_bp.add_url_rule(
    "/units_of_measurements",
    view_func=UnitsOfMeasurementListAPI.as_view("units_of_measurement_list"), methods=['GET']
)

directory_bp.add_url_rule(
    "/units_of_measurements/create",
    view_func=UnitsOfMeasurementCreateAPI.as_view("units_of_measurement_create"), methods=['POST']
)

directory_bp.add_url_rule(
    "/units_of_measurements/<int:id>",
    view_func=UnitsOfMeasurementDetailAPI.as_view("units_of_measurement_detail"), methods=['GET']
)

directory_bp.add_url_rule(
    "/units_of_measurements/<int:id>/update",
    view_func=UnitsOfMeasurementUpdateAPI.as_view("units_of_measurement_update"), methods=['PATCH']
)

directory_bp.add_url_rule(
    "/units_of_measurements/<int:id>/delete",
    view_func=UnitsOfMeasurementDeleteAPI.as_view("units_of_measurement_delete"), methods=['DELETE']
)



