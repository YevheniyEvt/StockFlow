from flaskr.documents.schemas import (
    DocumentItemResponseSchema,
    DocumentItemCreateSchema,
)
from flaskr.documents.services import DocumentItemService
from flaskr.core.views import CreateAPI

__all__ = (
    'DocumentItemCreateAPI',
)

class DocumentItemCreateAPI(CreateAPI):
    service = DocumentItemService
    request_schema = DocumentItemCreateSchema
    response_schema = DocumentItemResponseSchema