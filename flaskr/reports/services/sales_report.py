from decimal import Decimal
from typing import Any, Dict, List

from sqlalchemy import and_, func, select

from flaskr import db
from flaskr.accounting.accounting_enum import ProductMovementType
from flaskr.accounting.models import ProductMovement
from flaskr.nomenclature.models import Product

__all__ = (
    'SalesReportService',
)


class SalesReportService:

    @classmethod
    def create_report(cls, organization_id, data):
        start_date = data.start_date
        end_date = data.end_date

        stmt = (
            select(
                Product.id.label("product_id"),
                Product.name.label("product_name"),
                func.coalesce(func.sum(ProductMovement.quantity), 0).label("quantity"),
                func.coalesce(func.sum(ProductMovement.amount), 0).label("amount"),
            )
            .select_from(ProductMovement)
            .join(Product, Product.id == ProductMovement.product_id)
            .where(
                and_(
                    Product.organization_id == organization_id,
                    ProductMovement.movement_type == ProductMovementType.SELLING,
                    ProductMovement.created_at >= start_date,
                    ProductMovement.created_at <= end_date,
                )
            )
            .group_by(Product.id, Product.name)
            .order_by(Product.name)
        )

        rows = db.session.execute(stmt).all()

        items: List[Dict[str, Any]] = [
            {
                "product_id": r.product_id,
                "product_name": r.product_name,
                "quantity": r.quantity or Decimal("0"),
                "amount": r.amount or Decimal("0"),
            }
            for r in rows
        ]

        total_quantity = sum((i["quantity"] for i in items), Decimal("0"))
        total_amount = sum((i["amount"] for i in items), Decimal("0"))

        return {
            "start_date": start_date,
            "end_date": end_date,
            "total_quantity": total_quantity,
            "total_amount": total_amount,
            "items": items,
        }
