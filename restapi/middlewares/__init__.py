from __future__ import annotations
import json
from inspect import signature

from restapi.xmodels.request_base import AppData, RequestBase


class RequestMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.process_request(request)
        if response is not None:
            return response
        else:
            return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        view_signature = signature(view_func)
        annotation = view_signature.parameters['request'].annotation
        if '__origin__' in annotation.__dict__:
            origin = annotation.__origin__

            if origin == RequestBase:
                body_data = {}

                try:
                    body_data = json.loads(request.body)
                except Exception:
                    print("Request body is not json, we will try to populate using POST data.")
                    body_data = request.POST

                request.app_data = AppData[annotation.__args__[0]](annotation.__args__[0].parse_obj(body_data), 10, 20)
            elif origin is None:
                pass
            else:
                raise SystemError("unexpected annotation :s" % origin)

    def process_request(self, request):
        request.req_id = 1234
        request.app_data = None
