from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr.documents.models.document_enum import GoodsDeliveryNoteStatus
from flaskr.documents.schemas.document_item import DocumentItemResponseSchema


__all__ = (
    'GoodsDeliveryNoteUpdateSchema',
    'GoodsDeliveryNoteResponseSchema',
    'GoodsDeliveryNoteListSchema',
    'GoodsDeliveryNoteChangeStatusSchema',
    'GoodsDeliveryNoteCreateSchema',
)


class GoodsDeliveryNoteCreateSchema(BaseModel):
    organization_id: int
    counterparty_id: int
    invoice_id: int


class GoodsDeliveryNoteUpdateSchema(BaseModel):
    organization_id: int | None = None
    counterparty_id: int | None = None
    operation_type_id: int | None = None
    warehouse_id: int | None = None
    contract_id: int | None = None
    invoice_id: int | None = None
    comment: str | None = None


class GoodsDeliveryNoteChangeStatusSchema(BaseModel):
    status: GoodsDeliveryNoteStatus


class GoodsDeliveryNoteListSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None


class GoodsDeliveryNoteResponseSchema(BaseModel):
    id: int
    status: GoodsDeliveryNoteStatus
    organization_id: int | None
    counterparty_id: int | None
    operation_type_id: int | None
    warehouse_id: int | None
    contract_id: int | None
    invoice_id: int | None
    amount: float | None
    comment: str | None
    created_at: datetime
    updated_at: datetime
    items: List[DocumentItemResponseSchema] | None = None

    model_config = ConfigDict(from_attributes=True)