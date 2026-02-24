from datetime import datetime
from pydantic import BaseModel, ConfigDict

__all__ = (
    'UnitsOfMeasurementCreateSchema',
    'UnitsOfMeasurementUpdateSchema',
    'UnitsOfMeasurementResponseSchema',
    'UnitsOfMeasurementListSchema',
)


class UnitsOfMeasurementCreateSchema(BaseModel):
    name: str
    organization_id: int
    additional_data: str


class UnitsOfMeasurementUpdateSchema(BaseModel):
    name: str | None = None
    organization_id: int | None = None


class UnitsOfMeasurementListSchema(BaseModel):
    organization_id: int


class UnitsOfMeasurementResponseSchema(BaseModel):
    id: int
    name: str
    additional_data: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)