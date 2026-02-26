from flaskr.directory.schemas import (
    OrganizationCreateSchema,
    OrganizationUpdateSchema,
    OrganizationResponseSchema,
    OrganizationListSchema,
)
from flaskr.directory.services import OrganizationService
from flaskr.core.views import ListAPI, DetailAPI, CreateAPI, UpdateAPI, DeleteAPI

__all__ = (
    'OrganizationDetailAPI',
    'OrganizationListAPI',
    'OrganizationCreateAPI',
    'OrganizationUpdateAPI',
    'OrganizationDeleteAPI',
)


class OrganizationListAPI(ListAPI):
    service = OrganizationService
    request_schema = OrganizationListSchema
    response_schema = OrganizationResponseSchema


class OrganizationDetailAPI(DetailAPI):
    service = OrganizationService
    response_schema = OrganizationResponseSchema


class OrganizationCreateAPI(CreateAPI):
    service = OrganizationService
    request_schema = OrganizationCreateSchema
    response_schema = OrganizationResponseSchema


class OrganizationUpdateAPI(UpdateAPI):
    service = OrganizationService
    request_schema = OrganizationUpdateSchema
    response_schema = OrganizationResponseSchema


class OrganizationDeleteAPI(DeleteAPI):
    service = OrganizationService
