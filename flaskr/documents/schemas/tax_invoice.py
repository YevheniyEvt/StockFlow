from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

from flaskr.documents.schemas.document_item import DocumentItemResponseSchema
from flaskr.documents.models.document_enum import TaxInvoiceStatus
from flaskr.directory.schemas import (
    OrganizationResponseSchema,
    CounterpartyResponseSchema,
    WarehouseResponseSchema,
    OperationTypeResponseSchema,
    ContractResponseSchema
)


__all__ = (
    'TaxInvoiceUpdateSchema',
    'TaxInvoiceResponseSchema',
    'TaxInvoiceListSchema',
    'TaxInvoiceChangeStatusSchema',
    'TaxInvoiceCreateSchema',
)


class TaxInvoiceCreateSchema(BaseModel):
    organization_id: int
    counterparty_id: int | None = None
    goods_delivery_note_id: int


class TaxInvoiceUpdateSchema(BaseModel):
    organization_id: int | None = None
    counterparty_id: int | None = None
    operation_type_id: int | None = None
    warehouse_id: int | None = None
    contract_id: int | None = None
    comment: str | None = None
    document_date: datetime | None = None


class TaxInvoiceChangeStatusSchema(BaseModel):
    status: TaxInvoiceStatus


class TaxInvoiceListSchema(BaseModel):
    organization_id: int | None = None
    counterparty_id: int | None = None


class TaxInvoiceResponseSchema(BaseModel):
    id: int
    organization_id: int
    organization: OrganizationResponseSchema | None = None
    counterparty_id: int | None = None
    counterparty: CounterpartyResponseSchema | None = None
    status: TaxInvoiceStatus
    operation_type_id: int | None
    operation_type: OperationTypeResponseSchema | None = None
    warehouse_id: int | None
    warehouse: WarehouseResponseSchema | None = None
    contract_id: int | None
    contract: ContractResponseSchema | None = None
    amount: float | None
    items: List[DocumentItemResponseSchema] | None = None
    comment: str | None
    created_at: datetime
    updated_at: datetime
    document_date: datetime

    model_config = ConfigDict(from_attributes=True)