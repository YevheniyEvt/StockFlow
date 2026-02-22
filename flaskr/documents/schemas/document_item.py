from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict

__all__ = (
    'DocumentItemUpdateSchema',
    'DocumentItemResponseSchema',
    'DocumentItemListSchema',
)


class DocumentItemUpdateSchema(BaseModel):
    pass


class DocumentItemListSchema(BaseModel):
    pass


class DocumentItemResponseSchema(BaseModel):
    document_id: int


    model_config = ConfigDict(from_attributes=True)