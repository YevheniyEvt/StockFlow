from typing import List

from sqlalchemy import select

from flaskr import db
from flaskr.core.services import BaseService
from flaskr.directory.models import Organization


class OrganizationService(BaseService[Organization]):
    model = Organization

    @classmethod
    def all(cls) -> List[Organization]:
        return db.session.scalars(select(cls.model)).all()