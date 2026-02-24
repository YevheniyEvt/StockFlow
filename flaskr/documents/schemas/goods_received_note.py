from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from flaskr.directory.schemas import OperationTypeResponseSchema
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
    organization_id: int | None = None
    warehouse_id : int | None = None
    contract_id: int | None = None
    comment: str | None = None
    document_date: datetime | None = None
    operation_type: OperationTypeResponseSchema | None = None


class GoodsReceivedNoteChangeStatusSchema(BaseModel):
    status: GoodsReceivedNoteStatus


class GoodsReceivedNoteListSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None


class GoodsReceivedNoteResponseSchema(BaseModel):
    id: int
    status: GoodsReceivedNoteStatus
    document_date: datetime
    amount: Decimal
    comment: str | None = None
    created_at: datetime
    updated_at: datetime
    contract: "ContractResponseSchema"
    warehouse: "WarehouseResponseSchema"
    organization: "OrganizationResponseSchema"
    counterparty: "CounterpartyResponseSchema"
    operation_type: "OperationTypeResponseSchema"

    model_config = ConfigDict(from_attributes=True)

class HeldGoodsReceivedNoteSchema(BaseModel):
    pass