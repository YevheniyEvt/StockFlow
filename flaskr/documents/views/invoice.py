from flask import request, jsonify
from flaskr.documents.schemas import (
    InvoiceUpdateSchema,
    InvoiceResponseSchema,
    InvoiceListSchema,
    InvoiceChangeStatusSchema,
    InvoiceCreateSchema,
)
from flaskr.documents.services import InvoiceService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'InvoiceDetailAPI',
    'InvoiceListAPI',
    'InvoiceUpdateAPI',
    'InvoiceDeleteAPI',
    'InvoiceChangeStatusAPI',
    'InvoiceCreateAPI',
)


class InvoiceListAPI(ListAPI):
    service = InvoiceService
    request_schema = InvoiceListSchema
    response_schema = InvoiceResponseSchema


class InvoiceDetailAPI(DetailAPI):
    service = InvoiceService
    response_schema = InvoiceResponseSchema


class InvoiceCreateAPI(CreateAPI):
    service = InvoiceService
    request_schema = InvoiceCreateSchema
    response_schema = InvoiceResponseSchema

    
class InvoiceUpdateAPI(UpdateAPI):
    service = InvoiceService
    request_schema = InvoiceUpdateSchema
    response_schema = InvoiceResponseSchema


class InvoiceDeleteAPI(DeleteAPI):
    service = InvoiceService


class InvoiceChangeStatusAPI(UpdateAPI):
    service = InvoiceService
    request_schema = InvoiceChangeStatusSchema
    response_schema = InvoiceResponseSchema

    def patch(self, id):
        payload = request.get_json(silent=False)
        data = self.validate(payload)
        updated_instance = self.service.change_status(id, data.status.value)
        return self.serialize(updated_instance)