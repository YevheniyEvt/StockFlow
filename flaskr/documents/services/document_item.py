from pydantic import BaseModel
from sqlalchemy import select

from flaskr import db, Product, Service
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    DocumentItem,
)

__all__ = (
    'DocumentItemService',
)


class DocumentItemService(BaseService[DocumentItem]):
    model = DocumentItem

    @classmethod
    def create(cls, data: BaseModel) -> DocumentItem:
        document_item = DocumentItem(**data.model_dump())
        cls._set_item_price_amount(document_item)
        db.session.add(document_item)
        db.session.commit()
        db.session.refresh(document_item)
        return document_item

    @classmethod
    def _set_item_price_amount(cls, document_item: DocumentItem) -> None:
        if document_item.product_id:
            product = db.session.get(Product, document_item.product_id)
            document_item.selling_price = product.selling_price
            document_item.amount = document_item.quantity * product.selling_price
        if document_item.service_id:
            service = db.session.get(Service, document_item.service_id)
            document_item.selling_price = service.selling_price
            document_item.amount = document_item.quantity * service.selling_price


    @classmethod
    def all(cls, data: BaseModel):
        document_id = data.document_id
        return db.session.scalars(select(cls.model).where(cls.model.document_id == document_id)).all()