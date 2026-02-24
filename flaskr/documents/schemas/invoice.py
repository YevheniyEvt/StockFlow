from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr.documents.schemas.document_item import DocumentItemResponseSchema
from flaskr.documents.models.document_enum import InvoiceStatus

__all__ = (
    'InvoiceUpdateSchema',
    'InvoiceResponseSchema',
    'InvoiceListSchema',
    'InvoiceChangeStatusSchema',
    'InvoiceCreateSchema',
)


class InvoiceCreateSchema(BaseModel):
    organization_id: int
    counterparty_id: int
    order_id: int


class InvoiceUpdateSchema(BaseModel):
    payment_final_date: datetime | None = None
    operation_type_id: int | None = None
    warehouse_id: int | None = None
    contract_id: int | None = None
    comment: str | None = None
    document_date: datetime | None = None

class InvoiceChangeStatusSchema(BaseModel):
    status: InvoiceStatus


class InvoiceListSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None


class InvoiceResponseSchema(BaseModel):
    id: int
    status: InvoiceStatus
    items: List[DocumentItemResponseSchema]
    payment_final_date: datetime | None
    created_at: datetime
    updated_at: datetime
    operation_type_id: int | None
    warehouse_id: int | None
    contract_id: int | None
    amount: float | None
    comment: str | None

    model_config = ConfigDict(from_attributes=True)