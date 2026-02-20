from flaskr.nomenclature import nomenclature_bp

from flaskr.nomenclature.views import (
    ServiceDetailAPI,
    ServiceListAPI,
    ServiceUpdateAPI,
    ServiceCreateAPI,
    ServiceDeleteAPI,
)

nomenclature_bp.add_url_rule(
    "/services",
    view_func=ServiceListAPI.as_view("service_list"), methods=['GET']
)

nomenclature_bp.add_url_rule(
    "/services/create",
    view_func=ServiceCreateAPI.as_view("service_create"), methods=['POST']
)

nomenclature_bp.add_url_rule(
    "/services/<int:id>",
    view_func=ServiceDetailAPI.as_view("service_detail"), methods=['GET']
)

nomenclature_bp.add_url_rule(
    "/services/<int:id>/update",
    view_func=ServiceUpdateAPI.as_view("service_update"), methods=['PATCH']
)

nomenclature_bp.add_url_rule(
    "/services/<int:id>/delete",
    view_func=ServiceDeleteAPI.as_view("service_delete"), methods=['DELETE']
)



