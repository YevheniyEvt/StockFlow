from typing import List

from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.directory.models import (
    Counterparty,
    OperationType,
    Organization,
    Warehouse,
    UnitsOfMeasurement,
)

__all__ = (
    'OrganizationService',
    'CounterpartyService',
    'OperationTypeService',
    'WarehouseService',
    'UnitsOfMeasurementService'
)

class DirectoryServiceMixin:
    @classmethod
    def all(cls, data):
        organization_id = data.organization_id
        return db.session.scalars(select(cls.model).where(cls.model.organization_id == organization_id)).all()


class OrganizationService(BaseService[Organization]):
    model = Organization

    @staticmethod
    def all(*args) -> List[Organization]:
        return db.session.scalars(select(Organization)).all()


class CounterpartyService(DirectoryServiceMixin, BaseService[Counterparty]):
    model = Counterparty


class OperationTypeService(DirectoryServiceMixin, BaseService[OperationType]):
    model = OperationType


class WarehouseService(DirectoryServiceMixin, BaseService[Warehouse]):
    model = Warehouse


class UnitsOfMeasurementService(DirectoryServiceMixin, BaseService[UnitsOfMeasurement]):
    model = UnitsOfMeasurement
