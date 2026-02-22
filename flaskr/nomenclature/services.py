from flaskr.core.mixins import ServicesAllMixin
from flaskr.core.services import BaseService
from flaskr.nomenclature.models import (
    Product,
    Service,
)

__all__ = (
    'ProductService',
    'ServiceService',
)


class ProductService(ServicesAllMixin, BaseService[Product]):
    model = Product


class ServiceService(ServicesAllMixin, BaseService[Service]):
    model = Service