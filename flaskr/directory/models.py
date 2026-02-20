from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey

__all__ = (
    'Organization',
    'Counterparty',
    'Warehouse',
    'OperationType',
    'UnitsOfMeasurement',
)

from flaskr import db
from flaskr.models.mixins import CreatedUpdatedDateTimeMixin


class Organization(CreatedUpdatedDateTimeMixin, db.Model):
    __tablename__ = 'organization'

    name: Mapped[str] = mapped_column(String(50))
    address: Mapped[str | None]  = mapped_column(String(50))


class BaseDirectory:
    organization_id: Mapped[int] = mapped_column(ForeignKey('organization.id'))
    name: Mapped[str] = mapped_column(String(50))


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



