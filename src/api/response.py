from dataclasses import dataclass
from typing import Any


@dataclass
class Response:
    is_success: bool
    status_code: int
    message: str
    data: Any | None = None


class SuccessResponse(Response):
    def __init__(self, message: str, data: Any | None = None):
        super().__init__(True, 200, message, data)


class ErrorResponse(Response):
    def __init__(self, message: str):
        super().__init__(False, 400, message)
