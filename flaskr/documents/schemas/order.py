from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr.documents.models.document_enum import OrderStatus
from flaskr.documents.schemas.document_item import DocumentItemResponseSchema

__all__ = (
    'OrderUpdateSchema',
    'OrderResponseSchema',
    'OrderListSchema',
    'OrderChangeStatusSchema',
    'OrderCreateSchema',
)


class OrderCreateSchema(BaseModel):
    organization_id: int
    counterparty_id: int


class OrderUpdateSchema(BaseModel):
    counterparty_id: str | None = None
    operation_type_id: int | None = None
    warehouse_id: int | None = None
    contract_id: int | None = None
    comment: str | None = None
    document_date: datetime | None = None


class OrderChangeStatusSchema(BaseModel):
    status: OrderStatus


class OrderListSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None




class OrderResponseSchema(BaseModel):
    id: int
    status: OrderStatus
    items: List[DocumentItemResponseSchema] | None
    operation_type_id: int | None
    warehouse_id: int | None
    contract_id: int | None
    amount: float | None
    comment: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)