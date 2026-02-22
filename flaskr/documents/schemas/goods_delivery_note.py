from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr import DocumentItem
from flaskr.documents.models.document_enum import GoodsDeliveryNoteStatus

__all__ = (
    'GoodsDeliveryNoteUpdateSchema',
    'GoodsDeliveryNoteResponseSchema',
    'GoodsDeliveryNoteListSchema',
    'GoodsDeliveryNoteChangeStatusSchema',
    'GoodsDeliveryNoteCreateSchema',
)


class GoodsDeliveryNoteCreateSchema(BaseModel):
    counterparty_id: int


class GoodsDeliveryNoteUpdateSchema(BaseModel):
    pass


class GoodsDeliveryNoteChangeStatusSchema(BaseModel):
    status: GoodsDeliveryNoteStatus


class GoodsDeliveryNoteListSchema(BaseModel):
    invoice_id: int
    counterparty_id: int | None = None


class GoodsDeliveryNoteResponseSchema(BaseModel):
    id: int
    status: GoodsDeliveryNoteStatus
    # items: List[DocumentItem] | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)