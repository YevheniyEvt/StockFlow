from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.directory.models import Warehouse


class WarehouseService(BaseService[Warehouse]):
    model = Warehouse

    @staticmethod
    def all(data) -> list[Warehouse]:
        organization_id = data.organization_id
        return db.session.scalars(select(Warehouse).where(Warehouse.organization_id == organization_id)).all()