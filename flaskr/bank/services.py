from typing import List

from sqlalchemy import select

from flaskr import db, BankAccountCompany, BankAccountCounterparty, Currency
from flaskr.core.services import BaseService
from flaskr.documents.models import Order

__all__ = (
    'BankAccountCompanyService',
    'BankAccountCounterpartyService',
)


class BankAccountCompanyService(BaseService[Order]):
    model = BankAccountCompany

    def all(self, data) -> List[BankAccountCompany]:
        organization_id = data.organization_id
        return db.session.scalars(select(self.model).where(self.model.organization_id == organization_id)).all()


class BankAccountCounterpartyService(BaseService[Order]):
    model = BankAccountCounterparty

    def all(self, data) -> List[BankAccountCounterparty]:
        counterparty_id = data.counterparty_id
        return db.session.scalars(select(self.model).where(self.model.counterparty_id == counterparty_id)).all()


class CurrencyService(BaseService[Order]):
    model = Currency

    def all(self, data) -> List[Currency]:
        organization_id = data.organization_id
        return db.session.scalars(select(self.model).where(self.model.organization_id == organization_id)).all()