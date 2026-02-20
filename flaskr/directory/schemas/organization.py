from datetime import datetime
from pydantic import BaseModel, ConfigDict

__all__ = (
    'OrganizationCreateSchema',
    'OrganizationUpdateSchema',
    'OrganizationResponseSchema',
)


class OrganizationCreateSchema(BaseModel):
    name: str
    address: str | None = None


class OrganizationUpdateSchema(BaseModel):
    name: str | None = None
    address: str | None = None


class OrganizationResponseSchema(BaseModel):
    id: int
    name: str
    address: str
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)