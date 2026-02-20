from datetime import datetime
from pydantic import BaseModel, ConfigDict

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


class CounterpartyUpdateSchema(BaseModel):
    name: str | None = None
    address: str | None = None
    organization_id: int | None = None


class CounterpartyListSchema(BaseModel):
    organization_id: int


class CounterpartyResponseSchema(BaseModel):
    id: int
    name: str
    address: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)