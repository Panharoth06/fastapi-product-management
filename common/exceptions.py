# common/exceptions.py

from fastapi import Request
from .base_responses import BaseAPIResponse


class APIException(Exception):
    """
    Base class for custom API exceptions.
    """

    def __init__(self, message: str, status_code: int = 400, data=None):
        self.message = message
        self.status_code = status_code
        self.data = data


async def api_exception_handler(request: Request, exc: APIException):
    """
    Handles all custom APIExceptions using BaseAPIResponse.error
    """
    return BaseAPIResponse.error(
        request=request,
        message=exc.message,
        code=exc.status_code,
        data=exc.data,
    )


async def generic_exception_handler(request: Request, exc: Exception):
    """
    Handles all uncaught (unexpected) exceptions in a consistent format.
    """
    return BaseAPIResponse.error(
        request=request,
        message="Internal server error",
        code=500,
        data={"detail": str(exc)},
    )
