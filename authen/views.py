from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_world(request):
    from pprint import pprint
    headers = {}
    for key, value in request.META.items():
        if key.startswith('HTTP_'):
            header_name = key[5:].replace('_', '-').title()
            headers[header_name] = value
    pprint(headers)
    return HttpResponse("Hello, World!")