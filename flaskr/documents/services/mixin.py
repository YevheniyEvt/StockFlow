from sqlalchemy import select

from flaskr import db, DocumentItem


class DocumentsAllMixin:

    def all(self, data):
        stmt = select(self.model)
        if data.counterparty_id:
            stmt = stmt.where(self.model.counterparty_id == data.counterparty_id)
        else:
            stmt = stmt.where(self.model.organization_id == data.organization_id)

        notes = db.session.scalars(stmt).all()
        return notes


class CreateDocumentItemMixin:

    @classmethod
    def _create_document_item(cls, item, document_id):
        document_item = DocumentItem(
            document_id=document_id,
            product_id=item.product.id,
            service_id=item.service.id,
            quantity=item.quantity,
            price_per_unit=item.price_per_unit,
            amount=item.amount,
        )
        db.session.add(document_item)
        db.session.commit()
