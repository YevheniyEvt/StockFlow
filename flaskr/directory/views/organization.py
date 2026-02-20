from flask import request
from flask.views import MethodView

from flaskr.directory.schemas import (
    OrganizationCreateSchema,
    OrganizationUpdateSchema,
    OrganizationResponseSchema
)
from flaskr.directory.services import OrganizationService

__all__ = (
    'OrganizationDetailAPI',
    'OrganizationListAPI',
    'OrganizationCreateAPI',
    'OrganizationUpdateAPI',
    'OrganizationDeleteAPI',
)


class OrganizationListAPI(MethodView):

    def get(self):
        items = OrganizationService.all()
        return [OrganizationResponseSchema.model_validate(item).model_dump() for item in items]


class OrganizationDetailAPI(MethodView):

    def get(self, id):
        organization = OrganizationService.get_or_404(id)
        return OrganizationResponseSchema.model_validate(organization).model_dump()


class OrganizationCreateAPI(MethodView):

    def post(self):
        data = OrganizationCreateSchema.model_validate(request.json)
        organization = OrganizationService.create(data)
        return OrganizationResponseSchema.model_validate(organization).model_dump(), 201


class OrganizationUpdateAPI(MethodView):

    def patch(self, id):
        organization = OrganizationService.get_or_404(id)
        data = OrganizationUpdateSchema.model_validate(request.json)
        organization_update = OrganizationService.update(organization, data)
        return OrganizationResponseSchema.model_validate(organization_update).model_dump()


class OrganizationDeleteAPI(MethodView):

    def delete(self, id):
        organization = OrganizationService.get_or_404(id)
        OrganizationService.delete(organization)
        return '', 204