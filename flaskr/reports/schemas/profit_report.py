from datetime import datetime
from decimal import Decimal
from typing import List

from pydantic import BaseModel

__all__ = (
    'ProfitReportItemSchema',
    'ProfitReportRequestSchema',
    'ProfitReportResponseSchema',
)


class ProfitReportItemSchema(BaseModel):
    product_id: int
    product_name: str
    revenue: Decimal
    purchase_cost: Decimal
    profit: Decimal


class ProfitReportRequestSchema(BaseModel):
    start_date: datetime
    end_date: datetime


class ProfitReportResponseSchema(BaseModel):
    start_date: datetime
    end_date: datetime
    total_revenue: Decimal
    total_purchase_cost: Decimal
    total_profit: Decimal
    items: List[ProfitReportItemSchema]