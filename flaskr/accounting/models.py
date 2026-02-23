from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, ForeignKey, Numeric

from flaskr import db
from flaskr.accounting.accounting_enum import ProductMovementType, FinancialOperationsStatus
from flaskr.core.mixins import CreatedUpdatedDateTimeMixin

__all__ = (
    'ProductMovement',
    'ServiceMovement',
    'ProductStockLot',
    'ServiceStockLot',
    'FinancialOperations',
)

class BaseMovement:
    document_id: Mapped[int] = mapped_column(ForeignKey('document.id'), primary_key=True)
    warehouse_id: Mapped[int] = mapped_column(ForeignKey('warehouse.id'), primary_key=True)
    quantity: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    price: Mapped[Decimal |None] = mapped_column(Numeric(10, 2))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    movement_type: Mapped[ProductMovementType]  = mapped_column(Enum(ProductMovementType))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())


class ProductMovement(BaseMovement, db.Model):
    __tablename__ = 'product_movement'
    product_id: Mapped[int | None] = mapped_column(ForeignKey('product.id'), primary_key=True)


class ServiceMovement(BaseMovement, db.Model):
    __tablename__ = 'service_movement'
    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'), primary_key=True)


class BaseStockLot:
    warehouse_id: Mapped[int] = mapped_column(ForeignKey('warehouse.id'))
    product_movement_id: Mapped[int] = mapped_column(ForeignKey('product_movement.id'))
    quantity_total: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=1)
    quantity_remaining: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=1)
    purchase_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=1)


class ProductStockLot(BaseStockLot, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'product_stock_lot'
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))


class ServiceStockLot(BaseStockLot, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'service_stock_lot'
    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'))


class FinancialOperations(db.Model):
    __tablename__ = 'financial_operations'

    bank_account_company_id: Mapped[int] = mapped_column(ForeignKey('bank_account_company.id'), primary_key=True)
    type_of_operation_id: Mapped[int] = mapped_column(ForeignKey('operation_type.id'), primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey('document.id'), primary_key=True)
    status: Mapped[FinancialOperationsStatus] = mapped_column(Enum(FinancialOperationsStatus))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    date: Mapped[datetime] = mapped_column(default=datetime.now())