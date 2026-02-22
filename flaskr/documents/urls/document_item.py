from flaskr.documents import documents_bp

from flaskr.documents.views import (
    DocumentItemCreateAPI,
)

documents_bp.add_url_rule(
    "/document_item/create",
    view_func=DocumentItemCreateAPI.as_view("document_item_create"), methods=['POST']
)