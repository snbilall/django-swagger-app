from datetime import datetime
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from restapi.decorators.decorators import api_vieww, renderer_classes

from rest_framework.renderers import JSONRenderer

from restapi.xmodels.index_models import Snippet
from restapi.serializers.index_serializer import SnippetSerializer

from drf_yasg.utils import swagger_auto_schema

from restapi.xmodels.request_base import RequestBase


# @swagger_auto_schema(
#     method='get',
#     query_serializer=SnippetSerializer,
#     responses={200: SnippetSerializer(many=True)},
#     tags=['Users'],
# )
@api_vieww(['POST'])
@renderer_classes((JSONRenderer, ))
@csrf_exempt
def index(request: RequestBase[Snippet]):
    if request.method == 'GET':
        snippets = Snippet(created=datetime.now(),
                       title="title", code="new code", linenos=4,
                       language="en-us", style=False)
        serializer = SnippetSerializer(snippets)
        response = JsonResponse(serializer.data, status=200)
        return response
    elif request.method == 'POST':
        payload = {
            'title': request.app_data.body.title,
            'code': request.app_data.body.code,
            'linenos': request.app_data.body.linenos,
            'language': request.app_data.body.language,
            'style': request.app_data.body.style
        }
        return JsonResponse(data=payload, status=200)


@api_vieww(['POST'])
@renderer_classes((JSONRenderer, ))
@csrf_exempt
def index2(request):
    snippets = Snippet(created=datetime.now(),
                       title="title", code="new code", linenos=4,
                       language="en-us", style=False)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippets)
        response = JsonResponse(serializer.data, status=200)
        return response
    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except Exception as exc:
            print(exc)
        else:
            serializer = SnippetSerializer(data=data)
            if serializer.is_valid():
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
