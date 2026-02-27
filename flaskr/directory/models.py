from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr
from sqlalchemy import String, ForeignKey

from flaskr import db
from flaskr.core.mixins import CreatedUpdatedDateTimeMixin

__all__ = (
    'Organization',
    'Counterparty',
    'Warehouse',
    'OperationType',
    'UnitsOfMeasurement',
    'Contract',
)


class Organization(CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'organization'

    name: Mapped[str] = mapped_column(String(50))
    address: Mapped[str | None] = mapped_column(String(50))
    additional_data: Mapped[str] = mapped_column(String(50))


class BaseDirectory:
    @declared_attr
    def organization_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey('organization.id'))

    @declared_attr
    def name(cls) -> Mapped[str]:
        return mapped_column(String(50))

    @declared_attr
    def additional_data(cls) -> Mapped[str]:
        return mapped_column(String(50))


class Counterparty(BaseDirectory, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'counterparty'

    address: Mapped[str | None] = mapped_column(String(50))


class Warehouse(BaseDirectory, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'warehouse'

    address: Mapped[str | None] = mapped_column(String(50))


class OperationType(BaseDirectory, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'operation_type'


class UnitsOfMeasurement(BaseDirectory, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'units_of_measurement'


class Contract(BaseDirectory, CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'contract'