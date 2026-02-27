from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr.documents.models.document_enum import OrderStatus
from flaskr.documents.schemas.document_item import DocumentItemResponseSchema
from flaskr.directory.schemas import (
    OrganizationResponseSchema,
    CounterpartyResponseSchema,
    WarehouseResponseSchema,
    OperationTypeResponseSchema,
    ContractResponseSchema
)

__all__ = (
    'OrderUpdateSchema',
    'OrderResponseSchema',
    'OrderListSchema',
    'OrderChangeStatusSchema',
    'OrderCreateSchema',
)


class OrderCreateSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None


class OrderUpdateSchema(BaseModel):
    counterparty_id: int | None = None
    organization_id: int | None = None
    operation_type_id: int | None = None
    warehouse_id: int | None = None
    contract_id: int | None = None
    comment: str | None = None
    document_date: datetime | None = None


class OrderChangeStatusSchema(BaseModel):
    status: OrderStatus


class OrderListSchema(BaseModel):
    organization_id: int | None = None
    counterparty_id: int | None = None




class OrderResponseSchema(BaseModel):
    id: int
    status: OrderStatus
    items: List[DocumentItemResponseSchema] | None
    operation_type_id: int | None
    operation_type: OperationTypeResponseSchema | None = None
    warehouse_id: int | None
    warehouse: WarehouseResponseSchema | None = None
    contract_id: int | None
    contract: ContractResponseSchema | None = None
    organization_id: int
    organization: OrganizationResponseSchema | None = None
    counterparty_id: int | None = None
    counterparty: CounterpartyResponseSchema | None = None
    amount: float | None
    comment: str | None
    document_date: datetime
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)