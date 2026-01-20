# common/schemas.py

from typing import Generic, TypeVar, Optional
from datetime import datetime
from pydantic.generics import GenericModel

T = TypeVar("T")


class BaseAPIResponseModel(GenericModel, Generic[T]):
    error_code: int
    success: bool
    message: str
    data: Optional[T]
    path: str
    timestamp: datetime
