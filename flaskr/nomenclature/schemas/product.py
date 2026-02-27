from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field
from flaskr.directory.schemas import UnitsOfMeasurementResponseSchema

__all__ = (
    'ProductCreateSchema',
    'ProductUpdateSchema',
    'ProductListSchema',
    'ProductResponseSchema',
)

class ProductBaseSchema(BaseModel):
    name: str
    organization_id: int
    counterparty_id: int | None = None
    units_of_measurement_id: int
    article: int
    multiplicity: Decimal = Field(max_digits=10, decimal_places=2, default=Decimal("1.00"))
    selling_price: Decimal = Field(max_digits=10, decimal_places=2)
    minimum_stock: Decimal = Field(max_digits=10, decimal_places=2, default=Decimal("1.00"))


class ProductCreateSchema(ProductBaseSchema):
    pass


class ProductUpdateSchema(BaseModel):
    name: str | None = None
    organization_id: int | None = None
    counterparty_id: int | None = None
    units_of_measurement_id: int | None = None
    article: int | None = None
    multiplicity: Decimal | None = Field(max_digits=10, decimal_places=2, default=None)
    selling_price: Decimal | None = Field(max_digits=10, decimal_places=2, default=None)
    minimum_stock: Decimal | None = Field(max_digits=10, decimal_places=2, default=None)


class ProductListSchema(BaseModel):
    organization_id: int | None = None


class ProductResponseSchema(ProductBaseSchema):
    id: int
    name: str
    multiplicity: float
    selling_price: float
    organization_id: int | None = None
    counterparty_id: int | None = None
    units_of_measurement_id: int | None = None
    units_of_measurement: UnitsOfMeasurementResponseSchema | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)