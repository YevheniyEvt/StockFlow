from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict
from flaskr.bank.schemas import BankAccountCounterpartyResponseSchema

__all__ = (
    'CounterpartyCreateSchema',
    'CounterpartyUpdateSchema',
    'CounterpartyResponseSchema',
    'CounterpartyListSchema',
)


class CounterpartyCreateSchema(BaseModel):
    name: str
    address: str | None = None
    organization_id: int
    additional_data: str


class CounterpartyUpdateSchema(BaseModel):
    name: str | None = None
    address: str | None = None
    organization_id: int | None = None


class CounterpartyListSchema(BaseModel):
    organization_id: int | None = None


class CounterpartyResponseSchema(BaseModel):
    id: int
    name: str
    address: str | None = None
    bank_accounts: List[BankAccountCounterpartyResponseSchema] | None = None
    additional_data: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)