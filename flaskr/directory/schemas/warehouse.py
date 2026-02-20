from datetime import datetime
from pydantic import BaseModel, ConfigDict

__all__ = (
    'WarehouseCreateSchema',
    'WarehouseUpdateSchema',
    'WarehouseResponseSchema',
)


class WarehouseCreateSchema(BaseModel):
    name: str
    address: str | None = None
    organization_id: int


class WarehouseUpdateSchema(BaseModel):
    name: str | None
    address: str | None = None
    organization_id: int | None = None


class WarehouseListSchema(BaseModel):
    organization_id: int


class WarehouseResponseSchema(BaseModel):
    id: int
    name: str
    address: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)