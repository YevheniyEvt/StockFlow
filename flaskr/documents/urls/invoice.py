from flaskr.documents import documents_bp

from flaskr.documents.views import (
    InvoiceDetailAPI,
    InvoiceListAPI,
    InvoiceUpdateAPI,
    InvoiceChangeStatusAPI,
    InvoiceCreateAPI,
)

documents_bp.add_url_rule(
    "/invoices",
    view_func=InvoiceListAPI.as_view("invoice_list"), methods=['GET']
)

documents_bp.add_url_rule(
    "/invoices/<int:id>",
    view_func=InvoiceDetailAPI.as_view("invoice_detail"), methods=['GET']
)

documents_bp.add_url_rule(
    "/invoices/create",
    view_func=InvoiceCreateAPI.as_view("invoice_create"), methods=['POST']
)

documents_bp.add_url_rule(
    "/invoices/<int:id>/update",
    view_func=InvoiceUpdateAPI.as_view("invoice_update"), methods=['PATCH']
)

documents_bp.add_url_rule(
    "/invoices/<int:id>/update-status",
    view_func=InvoiceChangeStatusAPI.as_view("invoice_update_status"), methods=['PATCH']
)



