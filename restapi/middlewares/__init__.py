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
        if body_class is not None:
            request.body = body_class(request.body)

    def process_request(self, request):
        pass
