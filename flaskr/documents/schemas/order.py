from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr import DocumentItem
from flaskr.documents.models.document_enum import OrderStatus

__all__ = (
    'OrderUpdateSchema',
    'OrderResponseSchema',
    'OrderListSchema',
    'OrderChangeStatusSchema',
    'OrderCreateSchema',
)


class OrderCreateSchema(BaseModel):
    counterparty_id: int

class OrderUpdateSchema(BaseModel):
    counterparty_id: str | None = None


class OrderChangeStatusSchema(BaseModel):
    status: OrderStatus


class OrderListSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None


class OrderResponseSchema(BaseModel):
    id: int
    status: OrderStatus
    items: List["DocumentItemResponseSchema"] | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)