from datetime import datetime
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

from restapi.xmodels.index_models import Snippet
from restapi.serializers.index_serializer import SnippetSerializer


@csrf_exempt
def index(request):
    snippets = Snippet(created=datetime.now(),
                       title="title", code="new code", linenos=4,
                       language="en-us", style=False)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippets)
        token = get_token(request)
        response = JsonResponse(serializer.data, status=200)
        response.set_cookie("csrftoken", token)
        return response
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
