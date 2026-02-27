from flaskr.documents.schemas import (
    DocumentItemResponseSchema,
    DocumentItemCreateSchema,
    DocumentItemUpdateSchema,
)
from flaskr.documents.services import DocumentItemService
from flaskr.core.views import CreateAPI, UpdateAPI, DeleteAPI, DetailAPI

__all__ = (
    'DocumentItemCreateAPI',
    'DocumentItemUpdateAPI',
    'DocumentItemDeleteAPI',
    'DocumentItemDetailAPI',
)

class DocumentItemCreateAPI(CreateAPI):
    service = DocumentItemService
    request_schema = DocumentItemCreateSchema
    response_schema = DocumentItemResponseSchema

class DocumentItemUpdateAPI(UpdateAPI):
    service = DocumentItemService
    request_schema = DocumentItemUpdateSchema
    response_schema = DocumentItemResponseSchema

class DocumentItemDeleteAPI(DeleteAPI):
    service = DocumentItemService

class DocumentItemDetailAPI(DetailAPI):
    service = DocumentItemService
    response_schema = DocumentItemResponseSchema