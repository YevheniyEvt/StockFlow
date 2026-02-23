from flaskr import db, ProductMovement
from flaskr.accounting.accounting_enum import ProductMovementStatus
__all__ = (
    'ProductMovementService',
)


class ProductMovementService:
    model = ProductMovement

    @classmethod
    def create(cls, item: "DocumentItem", warehouse_id: int):
        product_movement = cls.model(
            warehouse_id=warehouse_id,
            product_id=item.product_id,
            document_id=item.document_id,
            status=ProductMovementStatus.SELLING,
            quantity=item.quantity,
            price_per_unit=item.price_per_unit,
            amount=item.amount,
        )
        db.session.add(product_movement)
        db.session.commit()


