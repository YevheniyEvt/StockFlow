from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel

__all__ = (
    'RemainingProductsReportItemSchema',
    'RemainingProductsReportRequestSchema',
    'RemainingProductsReportResponseSchema',
)


class RemainingProductsReportItemSchema(BaseModel):
    product_id: int
    product_name: str
    quantity_remaining: Decimal
    total_cost: Decimal
    average_cost: Decimal


class RemainingProductsReportRequestSchema(BaseModel):
    date: datetime


class RemainingProductsReportResponseSchema(BaseModel):
    date: datetime
    total_quantity: Decimal
    total_cost: Decimal
    items: List[RemainingProductsReportItemSchema]