from typing import Any, Optional
from fastapi.responses import JSONResponse
from fastapi import Request
from datetime import datetime, timezone


class BaseAPIResponse:
    """
    A utility class for creating consistent API responses.
    Includes timestamp and request path for better tracking.
    """

    @staticmethod
    def success(
        request: Request,
        data: Optional[Any] = None,
        message: str = "Request successful",
        code: int = 200
    ) -> JSONResponse:
        """
        Returns a standardized success response.
        """
        return JSONResponse(
            status_code=code,
            content={
                "success": True,
                "message": message,
                "data": data or {},
                "path": str(request.url.path),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        )

    @staticmethod
    def error(
        code: int,
        request: Request,
        message: str = "An error occurred",
        data: Optional[Any] = None
    ) -> JSONResponse:
        """
        Returns a standardized error response.
        """
        return JSONResponse(
            status_code=code,
            content={
                "success": False,
                "message": message,
                "data": data or {},
                "path": str(request.url.path),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        )
