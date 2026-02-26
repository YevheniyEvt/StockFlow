from datetime import datetime
from pydantic import BaseModel, ConfigDict

__all__ = (
    'ContractCreateSchema',
    'ContractUpdateSchema',
    'ContractResponseSchema',
    'ContractListSchema',
)


class ContractCreateSchema(BaseModel):
    name: str
    organization_id: int
    additional_data: str


class ContractUpdateSchema(BaseModel):
    name: str | None = None
    organization_id: int | None = None


class ContractListSchema(BaseModel):
    organization_id: int | None = None


class ContractResponseSchema(BaseModel):
    id: int
    name: str
    additional_data: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)