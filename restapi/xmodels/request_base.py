from rest_framework.request import Request

from typing import Any, Generic, TypeVar

T = TypeVar("T")  # will be api base models


class AppData(Generic[T]):
    body: T
    device: Any
    user: Any


class RequestBase(Request, Generic[T]):
    app_data: AppData[T]
