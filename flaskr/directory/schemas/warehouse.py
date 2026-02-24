from datetime import datetime
from pydantic import BaseModel, ConfigDict

__all__ = (
    'WarehouseCreateSchema',
    'WarehouseUpdateSchema',
    'WarehouseResponseSchema',
    'WarehouseListSchema',
)


class WarehouseCreateSchema(BaseModel):
    name: str
    address: str | None = None
    organization_id: int
    additional_data: str


class WarehouseUpdateSchema(BaseModel):
    name: str | None = None
    address: str | None = None
    organization_id: int | None = None


class WarehouseListSchema(BaseModel):
    organization_id: int


class WarehouseResponseSchema(BaseModel):
    id: int
    name: str
    address: str | None = None
    additional_data: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)