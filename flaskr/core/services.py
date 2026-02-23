import abc
from abc import abstractmethod
from typing import Type, TypeVar, Generic, List

from flask import abort
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase

from flaskr import db


ModelType = TypeVar("ModelType", bound=DeclarativeBase)


class BaseService(Generic[ModelType], abc.ABC):
    """
    Base class for CRUD operations on SQLAlchemy models.
    
    Subclasses must define the `model` attribute.
    Provides methods for common operations: create, update, delete, get by ID, and list all.
    """

    model: Type[ModelType] = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.model is None:
            raise NotImplementedError(
                f"{cls.__name__} must define `model` attribute"
            )

    @staticmethod
    def update(instance, data: BaseModel) -> ModelType:
        instance.update_from_json(data)
        db.session.commit()
        db.session.refresh(instance)
        return instance

    @staticmethod
    def delete(instance):
        db.session.delete(instance)
        db.session.commit()

    @classmethod
    def create(cls, data: BaseModel) -> ModelType:
        instance = cls.model(**data.model_dump())
        db.session.add(instance)
        db.session.commit()
        db.session.refresh(instance)
        return instance

    @classmethod
    def get_or_404(cls, id) -> ModelType:
        instance = db.session.get(cls.model, id)
        if not instance:
            abort(404)
        return instance


    @classmethod
    @abstractmethod
    def all(cls, data: BaseModel) -> list[ModelType]:
        """
        Get all instances of this service
        :param data: json from request
        :return: list of instances of this service
        """
        pass