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
    document_id: Mapped[int] = mapped_column(ForeignKey('document.id'))
    warehouse_id: Mapped[int] = mapped_column(ForeignKey('warehouse.id'))
    organization_id: Mapped[int] = mapped_column(ForeignKey('organization.id'))
    quantity: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    price: Mapped[Decimal |None] = mapped_column(Numeric(10, 2))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    movement_type: Mapped[ProductMovementType]  = mapped_column(Enum(ProductMovementType, native_enum=False))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)


class ProductMovement(BaseMovement, db.Model):
    __tablename__ = 'product_movement'
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))


class ServiceMovement(BaseMovement, db.Model):
    __tablename__ = 'service_movement'
    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'))


class BaseStockLot:
    warehouse_id: Mapped[int] = mapped_column(ForeignKey('warehouse.id'))
    quantity_total: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=1)
    quantity_remaining: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=1)
    purchase_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=1)


class ProductStockLot(BaseStockLot, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'product_stock_lot'
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    product_movement_id: Mapped[int] = mapped_column(ForeignKey('product_movement.id'))


class ServiceStockLot(BaseStockLot, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'service_stock_lot'
    service_id: Mapped[int] = mapped_column(ForeignKey('service.id'))
    service_movement_id: Mapped[int] = mapped_column(ForeignKey('service_movement.id'))

class FinancialOperations(db.Model):
    __tablename__ = 'financial_operations'

    bank_account_company_id: Mapped[int] = mapped_column(ForeignKey('bank_account_company.id'))
    type_of_operation_id: Mapped[int] = mapped_column(ForeignKey('operation_type.id'))
    document_id: Mapped[int] = mapped_column(ForeignKey('document.id'))
    status: Mapped[FinancialOperationsStatus] = mapped_column(Enum(FinancialOperationsStatus, native_enum=False))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    date: Mapped[datetime] = mapped_column(default=datetime.now)