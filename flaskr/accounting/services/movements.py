from flaskr import db
from flaskr.accounting.accounting_enum import ProductMovementType
from flaskr.accounting.models import ServiceMovement, ProductMovement
from flaskr.accounting.services.stock_lot import ProductStockLotService

__all__ = (
    'ProductMovementService',
    'ServiceMovementService',
    'MovementService',
)


class MovementService:
    """Service to delegate movement creation to product or service movement services."""

    @classmethod
    def create_purchase(cls, item: "DocumentItem", commit: bool = True):
        """Delegate creating a purchase movement for either a product or a service."""

        if item.product_id:
            ProductMovementService.create_purchase(item, commit=commit)
        elif item.service_id:
            ServiceMovementService.create_purchase(item, commit=commit)

    @classmethod
    def create_selling(cls, item: "DocumentItem", commit: bool = True):
        """Delegate creating a selling movement for either a product or a service."""

        if item.product_id:
            ProductMovementService.create_selling(item, commit=commit)
        elif item.service_id:
            ServiceMovementService.create_selling(item, commit=commit)


class ProductMovementService:
    """Service to handle product movement operations (purchases and sales)."""

    model = ProductMovement

    @classmethod
    def create_purchase(cls, item: "DocumentItem", commit: bool = True):
        """Create a purchase record for a product and add it to the stock lot."""

        product_movement = cls.model(
            organization_id=item.document.organization_id,
            warehouse_id=item.document.warehouse_id,
            product_id=item.product_id,
            document_id=item.document_id,
            movement_type=ProductMovementType.PURCHASE,
            quantity=item.quantity,
            price=item.purchase_price,
            amount=item.amount,
        )
        db.session.add(product_movement)
        db.session.flush()
        ProductStockLotService.set_on_stock(product_movement, commit=False)
        if commit:
            db.session.commit()


    @classmethod
    def create_selling(cls, item: "DocumentItem", commit: bool = True):
        """Handle product sale by allocating it from existing stock lots."""

        ProductStockLotService.create_selling(item)
        if commit:
            db.session.commit()


class ServiceMovementService:
    """Service to handle service movement operations (purchases and sales)."""

    model = ServiceMovement

    @classmethod
    def create_purchase(cls, item: "DocumentItem", commit: bool = True):
        """Create a purchase record for a service."""

        product_movement = cls.model(
            organization_id=item.document.organization_id,
            warehouse_id=item.document.warehouse_id,
            service_id=item.service_id,
            document_id=item.document_id,
            movement_type=ProductMovementType.PURCHASE,
            quantity=item.quantity,
            price=item.purchase_price,
            amount=item.amount,
        )
        db.session.add(product_movement)
        if commit:
            db.session.commit()


    @classmethod
    def create_selling(cls, item: "DocumentItem", commit: bool = True):
        """Create a selling record for a service."""

        movement = cls.model(
            organization_id=item.document.organization_id,
            warehouse_id=item.document.warehouse_id,
            service_id=item.service_id,
            document_id=item.document_id,
            movement_type=ProductMovementType.SELLING,
            quantity=item.quantity,
            price=item.selling_price,
            amount=item.amount,
        )
        db.session.add(movement)
        if commit:
            db.session.commit()
