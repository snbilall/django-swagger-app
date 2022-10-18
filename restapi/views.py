from datetime import datetime
from django.http import HttpResponse, JsonResponse

from restapi.xmodels.index_models import Snippet
from restapi.serializers.index_serializer import SnippetSerializer


def index(request):
    snippets = Snippet(created=datetime.now(),
                       title="title", code="new code", linenos=4,
                       language="en-us", style=False)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippets)
        return JsonResponse(serializer.data, status=200)
