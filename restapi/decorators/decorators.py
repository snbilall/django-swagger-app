from django.http import HttpResponse, UnreadablePostError
from rest_framework import decorators
from functools import wraps, update_wrapper


def trap_unreadable_post_error(view):
    @wraps(view)
    def inner(request, *args, **kwargs):
        try:
            return view(request, *args, **kwargs)
        except UnreadablePostError:
            return HttpResponse(status=500)
    return inner


def api_vieww(*args, **kwargs):
    def inner(func):
        wrapped_as_view = decorators.api_view(*args, **kwargs)(func)
        wrapped_as_view = trap_unreadable_post_error(wrapped_as_view)

        update_wrapper(wrapped_as_view, func)
        return wrapped_as_view
    return inner


def renderer_classes(*args, **kwargs):
    return decorators.renderer_classes(*args, **kwargs)
