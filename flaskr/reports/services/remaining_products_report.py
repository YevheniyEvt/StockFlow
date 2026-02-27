from datetime import datetime, time
from decimal import Decimal
from typing import Any, Dict, List

from sqlalchemy import and_, func, select

from flaskr import db
from flaskr.accounting.models import ProductStockLot
from flaskr.nomenclature.models import Product


__all__ = (
    'RemainingProductsReportService',
)


class RemainingProductsReportService:

    @classmethod
    def create_report(cls, organization_id, data):
        report_date = data.date
        report_datetime = datetime.combine(report_date, time.max)
        # Remaining quantities and costs by product based on stock lots existing up to the date
        stmt = (
            select(
                Product.id.label("product_id"),
                Product.name.label("product_name"),
                func.coalesce(func.sum(ProductStockLot.quantity_remaining), 0).label(
                    "quantity_remaining"
                ),
                func.coalesce(
                    func.sum(ProductStockLot.quantity_remaining * ProductStockLot.purchase_price),
                    0,
                ).label("total_cost"),
            )
            .select_from(ProductStockLot)
            .join(Product, Product.id == ProductStockLot.product_id)
            .where(
                and_(
                    Product.organization_id == organization_id,
                    # Approximate snapshot: only lots created on or before selected date
                    ProductStockLot.created_at <= report_datetime,
                )
            )
            .group_by(Product.id, Product.name)
            .order_by(Product.name)
        )

        rows = db.session.execute(stmt).all()

        items: List[Dict[str, Any]] = []
        total_quantity = Decimal("0")
        total_cost = Decimal("0")
        for r in rows:
            qty = r.quantity_remaining or Decimal("0")
            cost = r.total_cost or Decimal("0")
            avg_cost = Decimal("0")
            if qty and qty != 0:
                # Avoid division by zero; cast to Decimal
                avg_cost = (cost / qty).quantize(Decimal("0.01")) if qty else Decimal("0")

            items.append(
                {
                    "product_id": r.product_id,
                    "product_name": r.product_name,
                    "quantity_remaining": qty,
                    "total_cost": cost,
                    "average_cost": avg_cost,
                }
            )
            total_quantity += qty
            total_cost += cost

        return {
            "date": report_date,
            "total_quantity": total_quantity,
            "total_cost": total_cost,
            "items": items,
        }