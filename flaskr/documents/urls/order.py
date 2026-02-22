from flaskr.documents import documents_bp

from flaskr.documents.views import (
    OrderDetailAPI,
    OrderListAPI,
    OrderUpdateAPI,
    OrderChangeStatusAPI,
    OrderCreateAPI,
)

documents_bp.add_url_rule(
    "/orders",
    view_func=OrderListAPI.as_view("order_list"), methods=['GET']
)

documents_bp.add_url_rule(
    "/orders/<int:id>",
    view_func=OrderDetailAPI.as_view("order_detail"), methods=['GET']
)

documents_bp.add_url_rule(
    "/orders/create",
    view_func=OrderCreateAPI.as_view("order_create"), methods=['POST']
)

documents_bp.add_url_rule(
    "/orders/<int:id>/update",
    view_func=OrderUpdateAPI.as_view("order_update"), methods=['PATCH']
)

documents_bp.add_url_rule(
    "/orders/<int:id>/update-status",
    view_func=OrderChangeStatusAPI.as_view("order_update_status"), methods=['PATCH']
)



