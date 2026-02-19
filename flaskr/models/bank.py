from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from flaskr import db
from flaskr.models.mixins import CreatedUpdatedDateTimeMixin


__all__ = (
    'BankAccountCompany',
    'BankAccountCounterparty',
    'Currency',
)

class BaseBankAccount:
    name: Mapped[str] = mapped_column(String(50))
    checking_account: Mapped[str]
    mfi: Mapped[int]
    edrpou: Mapped[int]
    bank: Mapped[str]
    currency_id: Mapped[int] = mapped_column(ForeignKey('currency.id'))


class BankAccountCompany(BaseBankAccount, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'bank_account_company'

    organization_id: Mapped[int] = mapped_column(ForeignKey('organization.id'))
    currency: Mapped["Currency"] = relationship(back_populates="bank_account_company")


class BankAccountCounterparty(BaseBankAccount, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'bank_account_counterparty'

    counterparty_id: Mapped[int] = mapped_column(ForeignKey('counterparty.id'))
    currency: Mapped["Currency"] = relationship(back_populates="bank_account_counterparty")


class Currency(CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'currency'

    organization_id: Mapped[int] = mapped_column(ForeignKey('organization.id'))
    name: Mapped[str] = mapped_column(String(50))
    bank_account_company: Mapped["BankAccountCompany"] = relationship(back_populates="currency")
    bank_account_counterparty: Mapped["BankAccountCounterparty"] = relationship(back_populates="currency")
