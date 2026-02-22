from flaskr.documents.schemas import (
    OrderUpdateSchema,
    OrderResponseSchema,
    OrderListSchema,
    OrderChangeStatusSchema,
    OrderCreateSchema,
)
from flaskr.documents.services import OrderService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'OrderDetailAPI',
    'OrderListAPI',
    'OrderUpdateAPI',
    'OrderDeleteAPI',
    'OrderChangeStatusAPI',
    'OrderCreateAPI',
)


class OrderListAPI(ListAPI):
    service = OrderService
    request_schema = OrderListSchema
    response_schema = OrderResponseSchema


class OrderDetailAPI(DetailAPI):
    service = OrderService
    response_schema = OrderResponseSchema


class OrderCreateAPI(CreateAPI):
    service = OrderService
    request_schema = OrderCreateSchema
    response_schema = OrderResponseSchema


class OrderUpdateAPI(UpdateAPI):
    service = OrderService
    request_schema = OrderUpdateSchema
    response_schema = OrderResponseSchema


class OrderDeleteAPI(DeleteAPI):
    service = OrderService


class OrderChangeStatusAPI(UpdateAPI):
    service = OrderService
    request_schema = OrderChangeStatusSchema
    response_schema = OrderResponseSchema