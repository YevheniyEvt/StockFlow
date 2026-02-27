from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr.directory.schemas import (
    OrganizationResponseSchema,
    CounterpartyResponseSchema,
    WarehouseResponseSchema,
    OperationTypeResponseSchema,
    ContractResponseSchema
)
from flaskr.documents.models.document_enum import GoodsReceivedNoteStatus
from flaskr.documents.schemas.document_item import DocumentItemResponseSchema


__all__ = (
    'GoodsReceivedNoteUpdateSchema',
    'GoodsReceivedNoteResponseSchema',
    'GoodsReceivedNoteListSchema',
    'GoodsReceivedNoteChangeStatusSchema',
    'GoodsReceivedNoteCreateSchema',
)


class GoodsReceivedNoteCreateSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None


class GoodsReceivedNoteUpdateSchema(BaseModel):
    counterparty_id: int | None = None
    organization_id: int | None = None
    warehouse_id : int | None = None
    contract_id: int | None = None
    comment: str | None = None
    document_date: datetime | None = None
    operation_type_id: int | None = None


class GoodsReceivedNoteChangeStatusSchema(BaseModel):
    status: GoodsReceivedNoteStatus


class GoodsReceivedNoteListSchema(BaseModel):
    organization_id: int | None = None
    counterparty_id: int | None = None


class GoodsReceivedNoteResponseSchema(BaseModel):
    id: int
    status: GoodsReceivedNoteStatus
    document_date: datetime
    amount: float | None
    comment: str | None
    created_at: datetime
    updated_at: datetime
    contract_id: int | None
    contract: ContractResponseSchema | None = None
    warehouse_id: int | None
    warehouse: WarehouseResponseSchema | None = None
    organization_id: int
    organization: OrganizationResponseSchema | None = None
    counterparty_id: int | None
    counterparty: CounterpartyResponseSchema | None = None
    operation_type_id: int | None
    operation_type: OperationTypeResponseSchema | None = None
    items: List[DocumentItemResponseSchema] | None = None

    model_config = ConfigDict(from_attributes=True)

class HeldGoodsReceivedNoteSchema(BaseModel):
    pass