from flask import request
from flask.views import MethodView

from flaskr.core.views import BaseApi
from flaskr.reports.schemas import (
    SalesReportRequestSchema,
    ProfitReportRequestSchema,
    RemainingProductsReportRequestSchema,
    SalesReportResponseSchema,
    ProfitReportResponseSchema,
    RemainingProductsReportResponseSchema
)
from flaskr.reports.services import (
    SalesReportService,
    ProfitReportService,
    RemainingProductsReportService
)


class BaseReport(BaseApi):

    def get(self, organization_id):
        payload = request.args.to_dict()
        data = self.validate(payload)
        report = self.service.create_report(organization_id, data)
        return self.serialize(report)


class SalesReport(BaseReport, MethodView):
    request_schema = SalesReportRequestSchema
    response_schema = SalesReportResponseSchema
    service = SalesReportService


class ProfitReport(BaseReport, MethodView):
    request_schema = ProfitReportRequestSchema
    response_schema = ProfitReportResponseSchema
    service = ProfitReportService


class RemainingProductsReport(BaseReport, MethodView):
    request_schema = RemainingProductsReportRequestSchema
    response_schema = RemainingProductsReportResponseSchema
    service = RemainingProductsReportService
