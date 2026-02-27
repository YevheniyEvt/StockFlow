from flaskr.documents import documents_bp

from flaskr.documents.views import (
    DocumentItemCreateAPI,
    DocumentItemUpdateAPI,
    DocumentItemDeleteAPI,
    DocumentItemDetailAPI,
)

documents_bp.add_url_rule(
    "/document_item/create",
    view_func=DocumentItemCreateAPI.as_view("document_item_create"), methods=['POST']
)

documents_bp.add_url_rule(
    "/document_item/<int:id>",
    view_func=DocumentItemDetailAPI.as_view("document_item_detail"), methods=['GET']
)

documents_bp.add_url_rule(
    "/document_item/<int:id>/update",
    view_func=DocumentItemUpdateAPI.as_view("document_item_update"), methods=['PATCH']
)

documents_bp.add_url_rule(
    "/document_item/<int:id>/delete",
    view_func=DocumentItemDeleteAPI.as_view("document_item_delete"), methods=['DELETE']
)