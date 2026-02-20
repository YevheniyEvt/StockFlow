from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.directory.models import Counterparty


class CounterpartyService(BaseService[Counterparty]):
    model = Counterparty

    @staticmethod
    def all(data) -> list[Counterparty]:
        organization_id = data.organization_id
        return db.session.scalars(select(Counterparty).where(Counterparty.organization_id == organization_id)).all()