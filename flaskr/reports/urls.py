from flaskr.reports import reports_bp

from flaskr.reports.views import SalesReport, ProfitReport, RemainingProductsReport

reports_bp.add_url_rule(
    "/sales-report/<int:organization_id>",
    view_func=SalesReport.as_view("sales_report"), methods=['GET']
)

reports_bp.add_url_rule(
    "/profit-report/<int:organization_id>",
    view_func=ProfitReport.as_view("profit_report"), methods=['GET']
)

reports_bp.add_url_rule(
    "/remaining-products-report/<int:organization_id>",
    view_func=RemainingProductsReport.as_view("remaining_products_report"), methods=['GET']
)
