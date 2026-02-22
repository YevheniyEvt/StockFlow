from sqlalchemy import select

from flaskr import db

class DocumentsAllMixin:

    def all(self, data):
        stmt = select(self.model)
        if data.counterparty_id:
            stmt = stmt.where(self.model.counterparty_id == data.counterparty_id)
        else:
            stmt = stmt.where(self.model.organization_id == data.organization_id)

        notes = db.session.scalars(stmt).all()
        return notes
