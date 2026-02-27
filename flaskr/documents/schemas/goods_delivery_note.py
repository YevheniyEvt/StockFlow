from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr.documents.models.document_enum import GoodsDeliveryNoteStatus
from flaskr.documents.schemas.document_item import DocumentItemResponseSchema
from flaskr.directory.schemas import (
    OrganizationResponseSchema,
    CounterpartyResponseSchema,
    WarehouseResponseSchema,
    OperationTypeResponseSchema,
    ContractResponseSchema
)


__all__ = (
    'GoodsDeliveryNoteUpdateSchema',
    'GoodsDeliveryNoteResponseSchema',
    'GoodsDeliveryNoteListSchema',
    'GoodsDeliveryNoteChangeStatusSchema',
    'GoodsDeliveryNoteCreateSchema',
)


class GoodsDeliveryNoteCreateSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None
    invoice_id: int


class GoodsDeliveryNoteUpdateSchema(BaseModel):
    organization_id: int | None = None
    counterparty_id: int | None = None
    operation_type_id: int | None = None
    warehouse_id: int | None = None
    contract_id: int | None = None
    invoice_id: int | None = None
    comment: str | None = None
    document_date: datetime | None = None

class GoodsDeliveryNoteChangeStatusSchema(BaseModel):
    status: GoodsDeliveryNoteStatus


class GoodsDeliveryNoteListSchema(BaseModel):
    organization_id: int | None = None
    counterparty_id: int | None = None


class GoodsDeliveryNoteResponseSchema(BaseModel):
    id: int
    status: GoodsDeliveryNoteStatus
    organization_id: int | None
    organization: OrganizationResponseSchema | None = None
    counterparty_id: int | None
    counterparty: CounterpartyResponseSchema | None = None
    operation_type_id: int | None
    operation_type: OperationTypeResponseSchema | None = None
    warehouse_id: int | None
    warehouse: WarehouseResponseSchema | None = None
    contract_id: int | None
    contract: ContractResponseSchema | None = None
    invoice_id: int | None
    amount: float | None
    comment: str | None
    created_at: datetime
    updated_at: datetime
    document_date: datetime
    items: List[DocumentItemResponseSchema] | None = None

    model_config = ConfigDict(from_attributes=True)