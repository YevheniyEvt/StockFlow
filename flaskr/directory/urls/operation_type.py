from flaskr.directory import directory_bp

from flaskr.directory.views import (
    OperationTypeDetailAPI,
    OperationTypeListAPI,
    OperationTypeUpdateAPI,
    OperationTypeCreateAPI,
    OperationTypeDeleteAPI,
)

directory_bp.add_url_rule(
    "/operation_types",
    view_func=OperationTypeListAPI.as_view("operation_type_list"), methods=['GET']
)

directory_bp.add_url_rule(
    "/operation_types/create",
    view_func=OperationTypeCreateAPI.as_view("operation_type_create"), methods=['POST']
)

directory_bp.add_url_rule(
    "/operation_types/<int:id>",
    view_func=OperationTypeDetailAPI.as_view("operation_type_detail"), methods=['GET']
)

directory_bp.add_url_rule(
    "/operation_types/<int:id>/update",
    view_func=OperationTypeUpdateAPI.as_view("operation_type_update"), methods=['PATCH']
)

directory_bp.add_url_rule(
    "/operation_types/<int:id>/delete",
    view_func=OperationTypeDeleteAPI.as_view("operation_type_delete"), methods=['DELETE']
)



