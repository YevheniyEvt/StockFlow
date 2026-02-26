from sqlalchemy import select

from flaskr import db, DocumentItem


class DocumentsAllMixin:

    @classmethod
    def all(cls, data):
        stmt = select(cls.model)
        if data.counterparty_id:
            stmt = stmt.where(cls.model.counterparty_id == data.counterparty_id)
            return db.session.scalars(stmt).all()
        if data.organization_id:
            stmt = stmt.where(cls.model.organization_id == data.organization_id)
            return db.session.scalars(stmt).all()
        return db.session.scalars(stmt).all()


class CreateDocumentItemMixin:

    @classmethod
    def _create_document_item(cls, item, document_id):
        document_item = DocumentItem(
            document_id=document_id,
            product_id=item.product_id,
            service_id=item.service_id,
            quantity=item.quantity,
            selling_price=getattr(item, 'selling_price', None),
            purchase_price=getattr(item, 'purchase_price', None),
            amount=item.amount,
        )
        db.session.add(document_item)
