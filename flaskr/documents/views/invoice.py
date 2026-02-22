from flask import request
from flask.views import MethodView

from flaskr.documents.schemas import (
    InvoiceUpdateSchema,
    InvoiceResponseSchema,
    InvoiceListSchema,
    InvoiceChangeStatusSchema,
    InvoiceCreateSchema,
)
from flaskr.documents.services import InvoiceService

__all__ = (
    'InvoiceDetailAPI',
    'InvoiceListAPI',
    'InvoiceUpdateAPI',
    'InvoiceDeleteAPI',
    'InvoiceChangeStatusAPI',
    'InvoiceCreateAPI',
)


class InvoiceListAPI(MethodView):

    def get(self):
        data = InvoiceListSchema.model_validate(request.json)
        items = InvoiceService.all(data)
        return [InvoiceResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class InvoiceDetailAPI(MethodView):

    def get(self, id):
        invoice = InvoiceService.get_or_404(id)
        return InvoiceResponseSchema.model_validate(invoice).model_dump(mode='json')


class InvoiceCreateAPI(MethodView):

    def post(self):
        data = InvoiceCreateSchema.model_validate(request.json)
        invoice = InvoiceService.create(data)
        return InvoiceResponseSchema.model_validate(invoice).model_dump(mode='json'), 201
    
    
class InvoiceUpdateAPI(MethodView):

    def patch(self, id):
        invoice = InvoiceService.get_or_404(id)
        data = InvoiceUpdateSchema.model_validate(request.json)
        invoice_update = InvoiceService.update(invoice, data)
        return InvoiceResponseSchema.model_validate(invoice_update).model_dump(mode='json')


class InvoiceDeleteAPI(MethodView):

    def delete(self, id):
        invoice = InvoiceService.get_or_404(id)
        InvoiceService.delete(invoice)
        return '', 204


class InvoiceChangeStatusAPI(MethodView):

    def patch(self, id):
        invoice = InvoiceService.get_or_404(id)
        data = InvoiceChangeStatusSchema.model_validate(request.json)
        invoice_update = InvoiceService.change_status(invoice, data)
        return InvoiceResponseSchema.model_validate(invoice_update).model_dump(mode='json')