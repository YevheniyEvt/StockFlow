from datetime import datetime
from pydantic import BaseModel, ConfigDict

__all__ = (
    'BankAccountCompanyCreateSchema',
    'BankAccountCompanyUpdateSchema',
    'BankAccountCompanyResponseSchema',
    'BankAccountCompanyListSchema',
    'BankAccountCounterpartyCreateSchema',
    'BankAccountCounterpartyUpdateSchema',
    'BankAccountCounterpartyResponseSchema',
    'BankAccountCounterpartyListSchema',
    'CurrencyCreateSchema',
    'CurrencyUpdateSchema',
    'CurrencyListSchema',
    'CurrencyResponseSchema',
)


class BaseSchema(BaseModel):
    name: str | None = None
    checking_account: str | None = None
    mfi: int | None = None
    edrpou: int | None = None
    bank: str | None = None
    currency_id: int | None = None


class BankAccountCompanyCreateSchema(BaseSchema):
    organization_id: int


class BankAccountCompanyUpdateSchema(BaseSchema):
    pass


class BankAccountCompanyListSchema(BaseModel):
    organization_id: int


class BankAccountCompanyResponseSchema(BaseSchema):
    id: int
    organization_id: int
    currency: 'CurrencyResponseSchema | None' = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BankAccountCounterpartyCreateSchema(BaseSchema):
    counterparty_id: int


class BankAccountCounterpartyUpdateSchema(BaseSchema):
    pass


class BankAccountCounterpartyListSchema(BaseModel):
    counterparty_id: int


class BankAccountCounterpartyResponseSchema(BaseSchema):
    id: int
    counterparty_id: int
    currency: 'CurrencyResponseSchema | None' = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CurrencyCreateSchema(BaseModel):
    organization_id: int
    name: str


class CurrencyUpdateSchema(BaseModel):
    name: str


class CurrencyListSchema(BaseModel):
    organization_id: int


class CurrencyResponseSchema(BaseModel):
    id: int
    organization_id: int
    name: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
