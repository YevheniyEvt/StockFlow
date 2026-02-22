from flask import request
from flask.views import MethodView

from flaskr.documents.schemas import (
    TaxInvoiceUpdateSchema,
    TaxInvoiceResponseSchema,
    TaxInvoiceListSchema,
    TaxInvoiceChangeStatusSchema,
    TaxInvoiceCreateSchema,
)
from flaskr.documents.services import TaxInvoiceService

__all__ = (
    'TaxInvoiceDetailAPI',
    'TaxInvoiceListAPI',
    'TaxInvoiceUpdateAPI',
    'TaxInvoiceDeleteAPI',
    'TaxInvoiceChangeStatusAPI',
    'TaxInvoiceCreateAPI',
)


class TaxInvoiceListAPI(MethodView):

    def get(self):
        data = TaxInvoiceListSchema.model_validate(request.json)
        items = TaxInvoiceService.all(data)
        return [TaxInvoiceResponseSchema.model_validate(item).model_dump(mode='json') for item in items]


class TaxInvoiceDetailAPI(MethodView):

    def get(self, id):
        tax_invoice = TaxInvoiceService.get_or_404(id)
        return TaxInvoiceResponseSchema.model_validate(tax_invoice).model_dump(mode='json')

class TaxInvoiceCreateAPI(MethodView):

    def post(self):
        data = TaxInvoiceCreateSchema.model_validate(request.json)
        tax_invoice = TaxInvoiceService.create(data)
        return TaxInvoiceResponseSchema.model_validate(tax_invoice).model_dump(mode='json'), 201
    
    
class TaxInvoiceUpdateAPI(MethodView):

    def patch(self, id):
        tax_invoice = TaxInvoiceService.get_or_404(id)
        data = TaxInvoiceUpdateSchema.model_validate(request.json)
        tax_invoice_update = TaxInvoiceService.update(tax_invoice, data)
        return TaxInvoiceResponseSchema.model_validate(tax_invoice_update).model_dump(mode='json')


class TaxInvoiceDeleteAPI(MethodView):

    def delete(self, id):
        tax_invoice = TaxInvoiceService.get_or_404(id)
        TaxInvoiceService.delete(tax_invoice)
        return '', 204


class TaxInvoiceChangeStatusAPI(MethodView):

    def patch(self, id):
        tax_invoice = TaxInvoiceService.get_or_404(id)
        data = TaxInvoiceChangeStatusSchema.model_validate(request.json)
        tax_invoice_update = TaxInvoiceService.change_status(tax_invoice, data)
        return TaxInvoiceResponseSchema.model_validate(tax_invoice_update).model_dump(mode='json')