from flaskr.nomenclature.schemas import (
    ProductCreateSchema,
    ProductUpdateSchema,
    ProductResponseSchema
)
from flaskr.nomenclature.schemas import ProductListSchema
from flaskr.nomenclature.services import ProductService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'ProductDetailAPI',
    'ProductListAPI',
    'ProductCreateAPI',
    'ProductUpdateAPI',
    'ProductDeleteAPI',
)


class ProductListAPI(ListAPI):
    service = ProductService
    request_schema = ProductListSchema
    response_schema = ProductResponseSchema


class ProductDetailAPI(DetailAPI):
    service = ProductService
    response_schema = ProductResponseSchema


class ProductCreateAPI(CreateAPI):
    service = ProductService
    request_schema = ProductCreateSchema
    response_schema = ProductResponseSchema


class ProductUpdateAPI(UpdateAPI):
    service = ProductService
    request_schema = ProductUpdateSchema
    response_schema = ProductResponseSchema


class ProductDeleteAPI(DeleteAPI):
    service = ProductService