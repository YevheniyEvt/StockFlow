from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr import DocumentItem
from flaskr.documents.models.document_enum import TaxInvoiceStatus


__all__ = (
    'TaxInvoiceUpdateSchema',
    'TaxInvoiceResponseSchema',
    'TaxInvoiceListSchema',
    'TaxInvoiceChangeStatusSchema',
    'TaxInvoiceCreateSchema',
)


class TaxInvoiceCreateSchema(BaseModel):
    counterparty_id: int
    goods_delivery_note_id: int


class TaxInvoiceUpdateSchema(BaseModel):
    pass


class TaxInvoiceChangeStatusSchema(BaseModel):
    status: TaxInvoiceStatus


class TaxInvoiceListSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None


class TaxInvoiceResponseSchema(BaseModel):
    id: int
    status: TaxInvoiceStatus
    # items: List[DocumentItem] | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)