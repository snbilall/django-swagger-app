from rest_framework.request import Request

from typing import Any, Generic, TypeVar

T = TypeVar("T")  # will be api base models


class AppData(Generic[T]):

    def __init__(self, body: T, device: Any, user: Any):
        self.body = body
        self.device = device
        self.user = user


class RequestBase(Request, Generic[T]):

    def __init__(self, app_data: AppData[T], request, parsers=None, authenticators=None, negotiator=None, parser_context=None):
        super().__init__(request, parsers, authenticators, negotiator, parser_context)
        self.app_data = app_data
