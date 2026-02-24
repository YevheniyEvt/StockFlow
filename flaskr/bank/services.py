from typing import List

from sqlalchemy import select

from flaskr import db, BankAccountCompany, BankAccountCounterparty, Currency
from flaskr.core.services import BaseService
from flaskr.documents.models import Order

__all__ = (
    'BankAccountCompanyService',
    'BankAccountCounterpartyService',
)


class BankAccountCompanyService(BaseService[BankAccountCompany]):
    model = BankAccountCompany

    @classmethod
    def all(cls, data) -> List[BankAccountCompany]:
        organization_id = data.organization_id
        return db.session.scalars(select(cls.model).where(cls.model.organization_id == organization_id)).all()


class BankAccountCounterpartyService(BaseService[BankAccountCounterparty]):
    model = BankAccountCounterparty

    @classmethod
    def all(cls, data) -> List[BankAccountCounterparty]:
        counterparty_id = data.counterparty_id
        return db.session.scalars(select(cls.model).where(cls.model.counterparty_id == counterparty_id)).all()


class CurrencyService(BaseService[Currency]):
    model = Currency

    @classmethod
    def all(cls, data) -> List[Currency]:
        organization_id = data.organization_id
        return db.session.scalars(select(cls.model).where(cls.model.organization_id == organization_id)).all()