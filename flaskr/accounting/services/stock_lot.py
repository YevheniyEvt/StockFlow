from sqlalchemy import select

from flaskr import db
from flaskr.accounting.accounting_enum import ProductMovementType
from flaskr.accounting.models import ProductStockLot, ServiceStockLot, ProductMovement
from flaskr.core.mixins import BusinessError


__all__ = (
    'ProductStockLotService',
    'ServiceStockLotService',
)


class ProductStockLotService:
    """Service to handle product stock lot operations, such as adding to stock and selling."""

    model = ProductStockLot

    @classmethod
    def set_on_stock(cls, product_movement: "ProductMovement", commit: bool = True):
        """Create a new stock lot entry from a product movement (purchase)."""

        stock = cls.model(
            product_id=product_movement.product_id,
            warehouse_id=product_movement.warehouse_id,
            product_movement_id=product_movement.id,
            quantity_total=product_movement.quantity,
            quantity_remaining=product_movement.quantity,
            purchase_price=product_movement.price,
        )
        db.session.add(stock)
        if commit:
            db.session.commit()

    @classmethod
    def create_selling(cls, item: "DocumentItem"):
        """Handle selling from stock lots using FIFO (first-in-first-out) strategy."""

        stmt = (select(ProductStockLot)
                .where(
            ProductStockLot.product_id == item.product_id,
            ProductStockLot.warehouse_id == item.document.warehouse_id,
            ProductStockLot.quantity_remaining > 0,
                )
                .order_by(ProductStockLot.created_at.asc())
                .with_for_update()
        )
        lots = db.session.execute(stmt).scalars().all()
        qty_to_sell = item.quantity

        for lot in lots:
            if qty_to_sell <= 0:
                break

            available = lot.quantity_remaining
            sell_from_lot = min(available, qty_to_sell)

            lot.quantity_remaining -= sell_from_lot
            qty_to_sell -= sell_from_lot

            # We create a movement for each batch for accurate cost accounting
            movement = ProductMovement(
                warehouse_id=item.document.warehouse_id,
                product_id=item.product_id,
                document_id=item.document_id,
                movement_type=ProductMovementType.SELLING,
                quantity=sell_from_lot,
                price=lot.purchase_price,
                amount=sell_from_lot * lot.purchase_price,
            )
            db.session.add(movement)

        if qty_to_sell > 0:
            raise BusinessError(f"Не достатня кількість товару на складі: {item.product.name}. Операція відмінена")


class ServiceStockLotService:
    """Service to handle service stock lot operations (placeholder for consistency)."""

    model = ServiceStockLot
