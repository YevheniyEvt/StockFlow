from . import directory_bp

from flaskr.directory.views import (
    WarehouseDetailAPI,
    WarehouseListAPI,
    WarehouseUpdateAPI,
    WarehouseCreateAPI,
    WarehouseDeleteAPI,
)

directory_bp.add_url_rule(
    "/warehouses",
    view_func=WarehouseListAPI.as_view("warehouse_list"), methods=['GET']
)

directory_bp.add_url_rule(
    "/warehouses/create",
    view_func=WarehouseCreateAPI.as_view("warehouse_create"), methods=['POST']
)

directory_bp.add_url_rule(
    "/warehouses/<int:id>",
    view_func=WarehouseDetailAPI.as_view("warehouse_detail"), methods=['GET']
)

directory_bp.add_url_rule(
    "/warehouses/<int:id>/update",
    view_func=WarehouseUpdateAPI.as_view("warehouse_update"), methods=['PATCH']
)

directory_bp.add_url_rule(
    "/warehouses/<int:id>/delete",
    view_func=WarehouseDeleteAPI.as_view("warehouse_delete"), methods=['DELETE']
)



