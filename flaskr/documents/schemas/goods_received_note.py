from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr import DocumentItem
from flaskr.documents.models.document_enum import GoodsReceivedNoteStatus

__all__ = (
    'GoodsReceivedNoteUpdateSchema',
    'GoodsReceivedNoteResponseSchema',
    'GoodsReceivedNoteListSchema',
    'GoodsReceivedNoteChangeStatusSchema',
    'GoodsReceivedNoteCreateSchema',
)


class GoodsReceivedNoteCreateSchema(BaseModel):
    counterparty_id: int


class GoodsReceivedNoteUpdateSchema(BaseModel):
    counterparty_id: str | None = None


class GoodsReceivedNoteChangeStatusSchema(BaseModel):
    status: GoodsReceivedNoteStatus


class GoodsReceivedNoteListSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None


class GoodsReceivedNoteResponseSchema(BaseModel):
    id: int
    status: GoodsReceivedNoteStatus
    # items: List[DocumentItem] | None = None
    held_date: datetime | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)