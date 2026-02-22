from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr import DocumentItem
from flaskr.documents.models.document_enum import InvoiceStatus

__all__ = (
    'InvoiceUpdateSchema',
    'InvoiceResponseSchema',
    'InvoiceListSchema',
    'InvoiceChangeStatusSchema',
    'InvoiceCreateSchema',
)


class InvoiceCreateSchema(BaseModel):
    counterparty_id: int


class InvoiceUpdateSchema(BaseModel):
    payment_final_date: datetime | None = None


class InvoiceChangeStatusSchema(BaseModel):
    status: InvoiceStatus


class InvoiceListSchema(BaseModel):
    order_id: int
    counterparty_id: int | None = None


class InvoiceResponseSchema(BaseModel):
    id: int
    status: InvoiceStatus
    # items: List[DocumentItem] | None = None
    payment_final_date: datetime
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)