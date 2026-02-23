from decimal import Decimal

from pydantic import BaseModel, ConfigDict, model_validator

__all__ = (
    'DocumentItemUpdateSchema',
    'DocumentItemResponseSchema',
    'DocumentItemListSchema',
    'DocumentItemCreateSchema',
)

from flaskr.nomenclature.schemas import ProductResponseSchema, ServiceResponseSchema


class DocumentItemCreateSchema(BaseModel):
    document_id: int
    quantity: int
    product_id: int | None = None
    service_id: int | None = None

    @model_validator(mode='after')
    def check_product_or_service(self) -> DocumentItemCreateSchema:
        if self.product_id is None and self.service_id is None:
            raise ValueError('One of product_id or service_id must be provided')
        return self


class DocumentItemUpdateSchema(BaseModel):
    selling_price: int | None = None
    purchase_price: int | None = None
    quantity: int | None = None


class DocumentItemListSchema(BaseModel):
    pass


class DocumentItemResponseSchema(BaseModel):
    document_id: int
    product: ProductResponseSchema | None = None
    quantity: Decimal
    amount: Decimal
    service: ServiceResponseSchema | None = None

    model_config = ConfigDict(from_attributes=True)