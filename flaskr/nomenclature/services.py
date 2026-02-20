from flaskr.core.services import BaseService
from flaskr.nomenclature.models import (
    Product,
    Service,
)

__all__ = (
    'ProductService',
    'ServiceService',
)


class ProductService(BaseService[Product]):
    model = Product


class ServiceService(BaseService[Service]):
    model = Service