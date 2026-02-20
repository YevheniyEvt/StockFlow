from flask import request
from flask.views import MethodView

from flaskr.nomenclature.schemas import (
    ProductCreateSchema,
    ProductUpdateSchema,
    ProductResponseSchema
)
from flaskr.nomenclature.schemas import ProductListSchema
from flaskr.nomenclature.services import ProductService

__all__ = (
    'ProductDetailAPI',
    'ProductListAPI',
    'ProductCreateAPI',
    'ProductUpdateAPI',
    'ProductDeleteAPI',
)


class ProductListAPI(MethodView):

    def get(self):
        data = ProductListSchema.model_validate(request.json)
        items = ProductService.all(data)
        return [ProductResponseSchema.model_validate(item).model_dump() for item in items]


class ProductDetailAPI(MethodView):

    def get(self, id):
        product = ProductService.get_or_404(id)
        return ProductResponseSchema.model_validate(product).model_dump()


class ProductCreateAPI(MethodView):

    def post(self):
        data = ProductCreateSchema.model_validate(request.json)
        product = ProductService.create(data)
        return ProductResponseSchema.model_validate(product).model_dump(), 201


class ProductUpdateAPI(MethodView):

    def patch(self, id):
        product = ProductService.get_or_404(id)
        data = ProductUpdateSchema.model_validate(request.json)
        product_update = ProductService.update(product, data)
        return ProductResponseSchema.model_validate(product_update).model_dump()


class ProductDeleteAPI(MethodView):

    def delete(self, id):
        product = ProductService.get_or_404(id)
        ProductService.delete(product)
        return '', 204