from flask import request
from flask.views import MethodView

from flaskr.documents.schemas import (
    DocumentItemResponseSchema,
    DocumentItemCreateSchema,
)
from flaskr.documents.services import DocumentItemService

__all__ = (

    'DocumentItemCreateAPI',
)

class DocumentItemCreateAPI(MethodView):

    def post(self):
        data = DocumentItemCreateSchema.model_validate(request.json)
        order = DocumentItemService.create(data)
        return DocumentItemResponseSchema.model_validate(order).model_dump(mode='json'), 201