from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict
from flaskr.bank.schemas import BankAccountCompanyResponseSchema

__all__ = (
    'OrganizationCreateSchema',
    'OrganizationUpdateSchema',
    'OrganizationResponseSchema',
    'OrganizationListSchema',
)


class OrganizationCreateSchema(BaseModel):
    name: str
    address: str | None = None
    additional_data: str


class OrganizationUpdateSchema(BaseModel):
    name: str | None = None
    address: str | None = None


class OrganizationListSchema(BaseModel):
    pass


class OrganizationResponseSchema(BaseModel):
    id: int
    name: str
    address: str | None = None
    bank_accounts: List[BankAccountCompanyResponseSchema] | None = None
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)