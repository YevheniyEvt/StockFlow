from flask import request
from flask.views import MethodView

from flaskr.documents.schemas import (
    OrderUpdateSchema,
    OrderResponseSchema,
    OrderListSchema,
    OrderChangeStatusSchema,
    OrderCreateSchema,
)
from flaskr.documents.services import OrderService

__all__ = (
    'OrderDetailAPI',
    'OrderListAPI',
    'OrderUpdateAPI',
    'OrderDeleteAPI',
    'OrderChangeStatusAPI',
    'OrderCreateAPI',
)


class OrderListAPI(MethodView):

    def get(self):
        data = OrderListSchema.model_validate(request.json)
        items = OrderService.all(data)
        return [OrderResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class OrderDetailAPI(MethodView):

    def get(self, id):
        order = OrderService.get_or_404(id)
        return OrderResponseSchema.model_validate(order).model_dump(mode='json')

class OrderCreateAPI(MethodView):

    def post(self):
        data = OrderCreateSchema.model_validate(request.json)
        order = OrderService.create(data)
        return OrderResponseSchema.model_validate(order).model_dump(mode='json'), 201

class OrderUpdateAPI(MethodView):

    def patch(self, id):
        order = OrderService.get_or_404(id)
        data = OrderUpdateSchema.model_validate(request.json)
        order_update = OrderService.update(order, data)
        return OrderResponseSchema.model_validate(order_update).model_dump(mode='json')


class OrderDeleteAPI(MethodView):

    def delete(self, id):
        order = OrderService.get_or_404(id)
        OrderService.delete(order)
        return '', 204


class OrderChangeStatusAPI(MethodView):

    def patch(self, id):
        order = OrderService.get_or_404(id)
        data = OrderChangeStatusSchema.model_validate(request.json)
        order_update = OrderService.change_status(order, data)
        return OrderResponseSchema.model_validate(order_update).model_dump(mode='json')