from flaskr.nomenclature import nomenclature_bp

from flaskr.nomenclature.views import (
    ProductDetailAPI,
    ProductListAPI,
    ProductUpdateAPI,
    ProductCreateAPI,
    ProductDeleteAPI,
)

nomenclature_bp.add_url_rule(
    "/products",
    view_func=ProductListAPI.as_view("product_list"), methods=['GET']
)

nomenclature_bp.add_url_rule(
    "/products/create",
    view_func=ProductCreateAPI.as_view("product_create"), methods=['POST']
)

nomenclature_bp.add_url_rule(
    "/products/<int:id>",
    view_func=ProductDetailAPI.as_view("product_detail"), methods=['GET']
)

nomenclature_bp.add_url_rule(
    "/products/<int:id>/update",
    view_func=ProductUpdateAPI.as_view("product_update"), methods=['PATCH']
)

nomenclature_bp.add_url_rule(
    "/products/<int:id>/delete",
    view_func=ProductDeleteAPI.as_view("product_delete"), methods=['DELETE']
)



