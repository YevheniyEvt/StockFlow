from flask import request, jsonify
from flaskr.documents.schemas import (
    TaxInvoiceUpdateSchema,
    TaxInvoiceResponseSchema,
    TaxInvoiceListSchema,
    TaxInvoiceChangeStatusSchema,
    TaxInvoiceCreateSchema,
)
from flaskr.documents.services import TaxInvoiceService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'TaxInvoiceDetailAPI',
    'TaxInvoiceListAPI',
    'TaxInvoiceUpdateAPI',
    'TaxInvoiceDeleteAPI',
    'TaxInvoiceChangeStatusAPI',
    'TaxInvoiceCreateAPI',
)


class TaxInvoiceListAPI(ListAPI):
    service = TaxInvoiceService
    request_schema = TaxInvoiceListSchema
    response_schema = TaxInvoiceResponseSchema


class TaxInvoiceDetailAPI(DetailAPI):
    service = TaxInvoiceService
    response_schema = TaxInvoiceResponseSchema


class TaxInvoiceCreateAPI(CreateAPI):
    service = TaxInvoiceService
    request_schema = TaxInvoiceCreateSchema
    response_schema = TaxInvoiceResponseSchema
    
    
class TaxInvoiceUpdateAPI(UpdateAPI):
    service = TaxInvoiceService
    request_schema = TaxInvoiceUpdateSchema
    response_schema = TaxInvoiceResponseSchema


class TaxInvoiceDeleteAPI(DeleteAPI):
    service = TaxInvoiceService


class TaxInvoiceChangeStatusAPI(UpdateAPI):
    service = TaxInvoiceService
    request_schema = TaxInvoiceChangeStatusSchema
    response_schema = TaxInvoiceResponseSchema

    def patch(self, id):
        payload = request.get_json(silent=False)
        data = self.validate(payload)
        updated_instance = self.service.change_status(id, data.status.value)
        return self.serialize(updated_instance)