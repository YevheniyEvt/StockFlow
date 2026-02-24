from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel

__all__ = (
    'SalesReportItemSchema',
    'SalesReportRequestSchema',
    'SalesReportResponseSchema',
)


class SalesReportItemSchema(BaseModel):
    product_id: int
    product_name: str
    quantity: Decimal
    amount: Decimal


class SalesReportRequestSchema(BaseModel):
    start_date: datetime
    end_date: datetime


class SalesReportResponseSchema(BaseModel):
    start_date: datetime
    end_date: datetime
    total_quantity: Decimal
    total_amount: Decimal
    items: List[SalesReportItemSchema]
