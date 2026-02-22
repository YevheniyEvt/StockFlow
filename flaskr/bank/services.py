from typing import List

from sqlalchemy import select

from flaskr import db, BankAccountCompany, BankAccountCounterparty, Currency
from flaskr.core.services import BaseService
from flaskr.documents.models import (
    Order,
)

__all__ = (
    'BankAccountCompanyService',
    'BankAccountCounterpartyService',
)


class BankAccountCompanyService(BaseService[Order]):
    model = BankAccountCompany


class BankAccountCounterpartyService(BaseService[Order]):
    model = BankAccountCounterparty


class CurrencyService(BaseService[Order]):
    model = Currency