from datetime import datetime
from pydantic import BaseModel, ConfigDict

__all__ = (
    'OperationTypeCreateSchema',
    'OperationTypeUpdateSchema',
    'OperationTypeResponseSchema',
    'OperationTypeListSchema',
)


class OperationTypeCreateSchema(BaseModel):
    name: str
    organization_id: int
    additional_data: str


class OperationTypeUpdateSchema(BaseModel):
    name: str | None = None
    organization_id: int | None = None


class OperationTypeListSchema(BaseModel):
    organization_id: int


class OperationTypeResponseSchema(BaseModel):
    id: int
    name: str
    additional_data: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)