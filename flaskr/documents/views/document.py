from flask import request
from flask.views import MethodView

from flaskr.documents.schemas import DocumentCreateSchema
from flaskr.documents.services import DocumentService

__all__ = (
    'DocumentCreateAPI',
)


class DocumentCreateAPI(MethodView):

    def post(self):
        data = DocumentCreateSchema.model_validate(request.json)
        document = DocumentService.create(data)
        related_document = DocumentService.get_related_document(document)
        schema = DocumentService.get_response_schema(document)
        return schema.model_validate(related_document).model_dump(mode='json'), 201
