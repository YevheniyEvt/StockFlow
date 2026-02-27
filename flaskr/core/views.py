import abc
from typing import TypeVar, Generic

from flask import request
from flask.views import MethodView

from pydantic import BaseModel

from flaskr.core.services import BaseService


RequestSchema = TypeVar("RequestSchema", bound=BaseModel)
ResponseSchema = TypeVar("ResponseSchema", bound=BaseModel)
ServiceType = TypeVar("ServiceType", bound=BaseService)


class BaseApi(Generic[RequestSchema, ResponseSchema, ServiceType], abc.ABC):
    """
    Base class for API views providing generic serialization, validation, and attribute checking.

    Generic Parameters:
        RequestSchema: The Pydantic model used for validating incoming request data.
        ResponseSchema: The Pydantic model used for serializing outgoing response data.
        ServiceType: The service class responsible for business logic and data access.
    """

    request_schema: RequestSchema
    response_schema: ResponseSchema
    service: ServiceType
    _required_attributes: tuple[str, ...] = ()

    def __init__(self):
        super().__init__()
        for attr in self._required_attributes:
            if not hasattr(self, attr):
                raise AttributeError(
                    f"{self.__class__.__name__} must define `{attr}` attribute"
                )

    def serialize(self, obj):
        return self.response_schema.model_validate(obj).model_dump(mode='json')

    def serialize_many(self, items):
        return [self.serialize(item) for item in items]

    def validate(self, payload: dict):
        if self.request_schema is None:
            return None
        return self.request_schema.model_validate(payload)


class ListAPI(BaseApi, MethodView):
    """
    API view for retrieving a list of resources.

    Requires `service`, `request_schema`, and `response_schema` to be defined in subclasses.
    """

    _required_attributes = ('service', 'request_schema', 'response_schema')

    def get(self):
        payload = request.args.to_dict()
        if not payload:
            payload = request.get_json(silent=True) or {}
        data = self.validate(payload)
        items = self.service.all(data)
        return self.serialize_many(items)


class DetailAPI(BaseApi, MethodView):
    """
    API view for retrieving a single resource by its ID.

    Requires `service` and `response_schema` to be defined in subclasses.
    """

    _required_attributes = ('service', 'response_schema')

    def get(self, id):
        instance = self.service.get_or_404(id)
        return self.serialize(instance)


class CreateAPI(BaseApi, MethodView):
    """
    API view for creating a new resource.

    Requires `service`, `request_schema`, and `response_schema` to be defined in subclasses.
    """

    _required_attributes = ('service', 'request_schema', 'response_schema')

    def post(self):
        payload = request.get_json(silent=False)
        data = self.validate(payload)
        instance = self.service.create(data)
        return self.serialize(instance), 201


class UpdateAPI(BaseApi, MethodView):
    """
    API view for updating an existing resource by its ID.

    Requires `service`, `request_schema`, and `response_schema` to be defined in subclasses.
    """

    _required_attributes = ('service', 'request_schema', 'response_schema')

    def patch(self, id):
        instance = self.service.get_or_404(id)
        payload = request.get_json(silent=False)
        data = self.validate(payload)
        updated_instance = self.service.update(instance, data)
        return self.serialize(updated_instance)


class DeleteAPI(BaseApi, MethodView):
    """
    API view for deleting an existing resource by its ID.

    Requires `service` to be defined in subclasses.
    """

    _required_attributes = ('service',)

    def delete(self, id):
        instance = self.service.get_or_404(id)
        self.service.delete(instance)
        return '', 204
