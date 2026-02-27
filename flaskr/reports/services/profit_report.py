from datetime import datetime, time
from decimal import Decimal
from typing import Any, Dict, List

from sqlalchemy import and_, func, select

from flaskr import db
from flaskr.accounting.accounting_enum import ProductMovementType
from flaskr.accounting.models import ProductMovement
from flaskr.nomenclature.models import Product

__all__ = (
    'ProfitReportService',
)


class ProfitReportService:

    @classmethod
    def create_report(cls, organization_id, data):
        start_date = data.start_date
        end_date = data.end_date
        report_start_date = datetime.combine(start_date, time.min)
        report_end_date = datetime.combine(end_date, time.max)
        # Revenue per product (selling)
        revenue_stmt = (
            select(
                Product.id.label("product_id"),
                Product.name.label("product_name"),
                func.coalesce(func.sum(ProductMovement.amount), 0).label("revenue"),
            )
            .select_from(ProductMovement)
            .join(Product, Product.id == ProductMovement.product_id)
            .where(
                and_(
                    Product.organization_id == organization_id,
                    ProductMovement.movement_type == ProductMovementType.SELLING,
                    ProductMovement.created_at >= report_start_date,
                    ProductMovement.created_at <= report_end_date,
                )
            )
            .group_by(Product.id, Product.name)
        )
        revenue_rows = {r.product_id: r for r in db.session.execute(revenue_stmt).all()}

        # Purchase cost per product (simple approximation: sum of purchase amounts in period)
        cost_stmt = (
            select(
                Product.id.label("product_id"),
                func.coalesce(func.sum(ProductMovement.amount), 0).label("purchase_cost"),
            )
            .select_from(ProductMovement)
            .join(Product, Product.id == ProductMovement.product_id)
            .where(
                and_(
                    Product.organization_id == organization_id,
                    ProductMovement.movement_type == ProductMovementType.PURCHASE,
                    ProductMovement.created_at >= report_start_date,
                    ProductMovement.created_at <= report_end_date,
                )
            )
            .group_by(Product.id)
        )
        cost_rows = {r.product_id: r for r in db.session.execute(cost_stmt).all()}

        product_ids = set(revenue_rows.keys()) | set(cost_rows.keys())

        items: List[Dict[str, Any]] = []
        total_revenue = Decimal("0")
        total_purchase_cost = Decimal("0")

        for pid in sorted(product_ids):
            rev = getattr(revenue_rows.get(pid), "revenue", Decimal("0")) or Decimal("0")
            name = getattr(revenue_rows.get(pid), "product_name", None)
            cost = getattr(cost_rows.get(pid), "purchase_cost", Decimal("0")) or Decimal("0")

            if name is None:
                # Fetch name if only in cost side
                name = db.session.get(Product, pid).name if pid else ""

            profit = rev - cost
            total_revenue += rev
            total_purchase_cost += cost

            items.append(
                {
                    "product_id": pid,
                    "product_name": name,
                    "revenue": rev,
                    "purchase_cost": cost,
                    "profit": profit,
                }
            )

        return {
            "start_date": start_date,
            "end_date": end_date,
            "total_revenue": total_revenue,
            "total_purchase_cost": total_purchase_cost,
            "total_profit": total_revenue - total_purchase_cost,
            "items": items,
        }
