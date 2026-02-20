from typing import List

from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.directory.models import Counterparty, OperationType, Organization, Warehouse

__all__ = (
    'OrganizationService',
    'CounterpartyService',
    "OperationTypeService",
    "WarehouseService",
)

class OrganizationService(BaseService[Organization]):
    model = Organization

    @staticmethod
    def all(*args) -> List[Organization]:
        return db.session.scalars(select(Organization)).all()


class CounterpartyService(BaseService[Counterparty]):
    model = Counterparty


class OperationTypeService(BaseService[OperationType]):
    model = OperationType


class WarehouseService(BaseService[Warehouse]):
    model = Warehouse
