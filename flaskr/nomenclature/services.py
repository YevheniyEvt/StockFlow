from flaskr.core.services import BaseService
from flaskr.nomenclature.models import (
    Product,
    Service,
)

__all__ = (
    'ProductService',
    'ServicesService',
)


class ProductService(BaseService[Product]):
    model = Product


class ServicesService(BaseService[Service]):
    model = Service