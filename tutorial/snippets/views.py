from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.shortcuts import render

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content in JSON
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content-type'] = 'application/JSON'
        super(JSONResponse, self).__init__(content, **kwargs)

    @csrf_exempt
    def snippet_list(request):
        """
        List all code snippets or create a new one
        """
        if request.method == "GET":
            snippets = Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many=True)
            return JSONResponse(serializer.data)

        elif request.method == "POST":
            data = JSONParser().parse(request)
            serializer = SnippetSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def snippet_detail(pk, request):
        """
        Retrieve, update, or delete a snippet
        """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":

    elif request.method == "PUT":

    elif request.method == "DELETE":

