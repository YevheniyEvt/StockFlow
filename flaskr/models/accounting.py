import enum
from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, ForeignKey, Numeric

__all__ = (
    'ProductMovement',
    'FinancialOperations',
)

from flaskr import db

class ProductMovementStatus(enum.Enum):
    selling = "selling"
    purchase = "purchase"

class ProductMovement(db.Model):
    __tablename__ = 'product_movement'

    warehouse_id: Mapped[int] = mapped_column(ForeignKey('warehouses.id'), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey('documents.id'), primary_key=True)
    status: Mapped[ProductMovementStatus]  = mapped_column(Enum(ProductMovementStatus))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    date: Mapped[datetime] = mapped_column(default=datetime.now())


class FinancialOperationsStatus(enum.Enum):
    debiting = "debiting"
    crediting = "crediting"

class FinancialOperations(db.Model):
    __tablename__ = 'financial_operations'

    type_of_operation_id: Mapped[int] = mapped_column(ForeignKey('operation_type.id'), primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey('documents.id'), primary_key=True)
    status: Mapped[FinancialOperationsStatus] = mapped_column(Enum(FinancialOperationsStatus))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    date: Mapped[datetime] = mapped_column(default=datetime.now())
