from datetime import datetime
from decimal import Decimal

from sqlalchemy import Numeric, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, declared_attr


class CreatedUpdatedDateTimeMixin:
    """Mixin to auto add created_at and updated_at columns"""

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(onupdate=datetime.now)


class ItemsMixin:
    quantity: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    price_per_unit: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    @declared_attr.directive
    def __table_args__(cls):
        return (
            CheckConstraint("quantity >= 0", name=f"ck_{cls.__tablename__}_quantity_positive"),
            CheckConstraint("price_per_unit >= 0", ame=f"ck_{cls.__tablename__}_price_per_unit_positive"),
        )