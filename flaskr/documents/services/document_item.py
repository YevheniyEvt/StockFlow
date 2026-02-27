from pydantic import BaseModel
from sqlalchemy import select

from flaskr import db, Product, Service, Document
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
        db.session.flush()
        cls._update_document_amount(document_item.document_id)
        db.session.commit()
        db.session.refresh(document_item)
        return document_item

    @classmethod
    def update(cls, instance: DocumentItem, data: BaseModel) -> DocumentItem:
        instance.update_from_json(data)
        cls._set_item_price_amount(instance)
        db.session.flush()
        cls._update_document_amount(instance.document_id)
        db.session.commit()
        db.session.refresh(instance)
        return instance

    @classmethod
    def delete(cls, instance: DocumentItem):
        document_id = instance.document_id
        db.session.delete(instance)
        db.session.flush()
        cls._update_document_amount(document_id)
        db.session.commit()

    @classmethod
    def _set_item_price_amount(cls, document_item: DocumentItem) -> None:
        if document_item.product_id:
            product = db.session.get(Product, document_item.product_id)
            if document_item.selling_price is None:
                document_item.selling_price = product.selling_price
            if document_item.purchase_price is None:
                document_item.purchase_price = product.selling_price
            document_item.amount = document_item.quantity * document_item.selling_price
        if document_item.service_id:
            service = db.session.get(Service, document_item.service_id)
            if document_item.selling_price is None:
                document_item.selling_price = service.selling_price
            document_item.amount = document_item.quantity * document_item.selling_price

    @classmethod
    def _update_document_amount(cls, document_id: int) -> None:
        document = db.session.get(Document, document_id)
        if document:
            total_amount = db.session.scalar(
                select(db.func.sum(DocumentItem.amount)).where(DocumentItem.document_id == document_id)
            ) or 0
            document.amount = total_amount


    @classmethod
    def all(cls, data: BaseModel):
        document_id = data.document_id
        return db.session.scalars(select(cls.model).where(cls.model.document_id == document_id)).all()