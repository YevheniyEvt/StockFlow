from datetime import datetime
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy import Numeric, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from flaskr import db

class CreatedUpdatedDateTimeMixin:
    """
    Mixin providing created_at and updated_at datetime columns.
    
    Automatically tracks row creation and last modification times.
    """

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)


class ItemsMixin:
    """
    Mixin for document items containing quantity, price per unit, and total amount.
    
    Includes basic check constraints to ensure quantity and price are non-negative.
    """

    quantity: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    purchase_price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2))
    selling_price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    discount: Mapped[Decimal] = mapped_column(Numeric(2,0), default=0)

    @declared_attr.directive
    def __table_args__(cls):
        return (
            CheckConstraint("quantity >= 0", name=f"ck_{cls.__tablename__}_quantity_positive"),
            CheckConstraint("purchase_price >= 0", name=f"ck_{cls.__tablename__}_purchase_price_positive"),
            CheckConstraint("selling_price >= 0", name=f"ck_{cls.__tablename__}_selling_price_positive"),
        )



class ServicesAllMixin:
    @classmethod
    def all(cls, data):
        if data and hasattr(data, 'organization_id') and data.organization_id:
            return db.session.scalars(
                select(cls.model).where(cls.model.organization_id == data.organization_id)
            ).all()
        return db.session.scalars(select(cls.model)).all()


class BusinessError(Exception):
    pass