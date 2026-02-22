from typing import List

from sqlalchemy import select

from flaskr.core.services import BaseService
from flaskr.documents.models import (
    Document,
)
from flaskr.documents.models.document_enum import DocumentType
from flaskr import db, GoodsReceivedNote, Order, Invoice, GoodsDeliveryNote, TaxInvoice
from flaskr.documents.schemas import (
    OrderResponseSchema, InvoiceResponseSchema, TaxInvoiceResponseSchema,
    GoodsDeliveryNoteResponseSchema, GoodsReceivedNoteResponseSchema
)

__all__ = (
    'DocumentService',
)


DOCUMENT_TYPE_RESPONSE_SCHEMA = {
    DocumentType.GOODS_RECEIVED_NOTE: GoodsReceivedNoteResponseSchema,
    DocumentType.ORDER: OrderResponseSchema,
    DocumentType.INVOICE: InvoiceResponseSchema,
    DocumentType.GOODS_DELIVERY_NOTE: GoodsDeliveryNoteResponseSchema,
    DocumentType.TAX_INVOICE: TaxInvoiceResponseSchema,
}

DOCUMENT_TYPE_RELATED_MODEL = {
    DocumentType.GOODS_RECEIVED_NOTE: GoodsReceivedNote,
    DocumentType.ORDER: Order,
    DocumentType.INVOICE: Invoice,
    DocumentType.GOODS_DELIVERY_NOTE: GoodsDeliveryNote,
    DocumentType.TAX_INVOICE: TaxInvoice,
}


class DocumentService(BaseService[Document]):
    model = Document

    @staticmethod
    def create(data) -> Document:
        document = Document(**data.model_dump())
        db.session.add(document)
        db.session.commit()
        return document

    @staticmethod
    def get_response_schema(document: Document) ->  (
            GoodsReceivedNoteResponseSchema | OrderResponseSchema |
            InvoiceResponseSchema | GoodsDeliveryNoteResponseSchema |
            TaxInvoiceResponseSchema
    ):
        return DOCUMENT_TYPE_RESPONSE_SCHEMA.get(document.document_type)


    @staticmethod
    def get_related_document(document: Document) -> (
            GoodsReceivedNote | Order | Invoice | GoodsDeliveryNote | TaxInvoice
    ):
        related_model = DOCUMENT_TYPE_RELATED_MODEL.get(document.document_type)
        return db.session.get(related_model, document.id)
