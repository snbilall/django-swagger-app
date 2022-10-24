import json


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
        body_class = getattr(view_func, 'body_class', None)

        body_data = {}

        try:
            body_data = json.loads(request.body)
        except Exception:
            print("Request body is not json, we will try to populate using POST data.")
            body_data = request.POST
        if body_class is not None:
            casted_body = body_class.parse_obj(body_data)
            request.casted_body = casted_body

    def process_request(self, request):
        request.req_id = 1234
        request.casted_body = None
