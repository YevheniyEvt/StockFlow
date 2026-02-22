from pydantic import BaseModel

__all__ = (
    'DocumentCreateSchema',
)

from flaskr.documents.models.document_enum import DocumentType


class DocumentCreateSchema(BaseModel):
    document_type: DocumentType
    counterparty_id: int