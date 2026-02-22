from flaskr.documents import documents_bp

from flaskr.documents.views import (
    DocumentCreateAPI,
)

documents_bp.add_url_rule(
    "/create",
    view_func=DocumentCreateAPI.as_view("document_create"), methods=['POST']
)



