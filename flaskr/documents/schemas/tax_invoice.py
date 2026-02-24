from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr.documents.schemas.document_item import DocumentItemResponseSchema
from flaskr.documents.models.document_enum import TaxInvoiceStatus


__all__ = (
    'TaxInvoiceUpdateSchema',
    'TaxInvoiceResponseSchema',
    'TaxInvoiceListSchema',
    'TaxInvoiceChangeStatusSchema',
    'TaxInvoiceCreateSchema',
)


class TaxInvoiceCreateSchema(BaseModel):
    organization_id: int
    counterparty_id: int
    goods_delivery_note_id: int


class TaxInvoiceUpdateSchema(BaseModel):
    operation_type_id: int | None = None
    warehouse_id: int | None = None
    contract_id: int | None = None
    comment: str | None = None
    document_date: datetime | None = None


class TaxInvoiceChangeStatusSchema(BaseModel):
    status: TaxInvoiceStatus


class TaxInvoiceListSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None


class TaxInvoiceResponseSchema(BaseModel):
    id: int
    status: TaxInvoiceStatus
    operation_type_id: int | None
    warehouse_id: int | None
    contract_id: int | None
    amount: float | None
    items: List[DocumentItemResponseSchema] | None = None
    comment: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)