from typing import List

from sqlalchemy import select

from flaskr import db
from flaskr.core.mixins import ServicesAllMixin
from flaskr.core.services import BaseService
from flaskr.directory.models import (
    Counterparty,
    OperationType,
    Organization,
    Warehouse,
    UnitsOfMeasurement,
    Contract,
)

__all__ = (
    'OrganizationService',
    'CounterpartyService',
    'OperationTypeService',
    'WarehouseService',
    'UnitsOfMeasurementService',
    'ContractService',
)


class OrganizationService(ServicesAllMixin, BaseService[Organization]):
    model = Organization


class CounterpartyService(ServicesAllMixin, BaseService[Counterparty]):
    model = Counterparty


class OperationTypeService(ServicesAllMixin, BaseService[OperationType]):
    model = OperationType


class WarehouseService(ServicesAllMixin, BaseService[Warehouse]):
    model = Warehouse


class UnitsOfMeasurementService(ServicesAllMixin, BaseService[UnitsOfMeasurement]):
    model = UnitsOfMeasurement


class ContractService(ServicesAllMixin, BaseService[UnitsOfMeasurement]):
    model = Contract