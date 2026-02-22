from flaskr.documents import documents_bp

from flaskr.documents.views import (
    TaxInvoiceDetailAPI,
    TaxInvoiceListAPI,
    TaxInvoiceUpdateAPI,
    TaxInvoiceChangeStatusAPI,
    TaxInvoiceCreateAPI,
)

documents_bp.add_url_rule(
    "/tax_invoices",
    view_func=TaxInvoiceListAPI.as_view("tax_invoice_list"), methods=['GET']
)

documents_bp.add_url_rule(
    "/tax_invoices/<int:id>",
    view_func=TaxInvoiceDetailAPI.as_view("tax_invoice_detail"), methods=['GET']
)

documents_bp.add_url_rule(
    "/tax_invoices/create",
    view_func=TaxInvoiceCreateAPI.as_view("tax_invoice_create"), methods=['POST']
)

documents_bp.add_url_rule(
    "/tax_invoices/<int:id>/update",
    view_func=TaxInvoiceUpdateAPI.as_view("tax_invoice_update"), methods=['PATCH']
)

documents_bp.add_url_rule(
    "/tax_invoices/<int:id>/update-status",
    view_func=TaxInvoiceChangeStatusAPI.as_view("tax_invoice_update_status"), methods=['PATCH']
)



