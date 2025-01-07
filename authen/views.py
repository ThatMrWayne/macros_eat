from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny



# Create your views here.
# test view
'''
def hello_world(request):
    from pprint import pprint
    headers = {}
    for key, value in request.META.items():
        if key.startswith('HTTP_'):
            header_name = key[5:].replace('_', '-').title()
            headers[header_name] = value
    pprint(headers)
    return HttpResponse("Hello, World!")
'''


@api_view(['POST']) # already csrf_exempt in DRF APIview
@permission_classes([
    AllowAny,
])
def signup(request):
    signup_data = request.data
    email = signup_data.get('email', None)
    name = signup_data.get('name', None)
    password = signup_data.get('password', None)
    identity = signup_data.get('identity', None)
    return Response(data={'status':'ok'}, status=status.HTTP_200_OK)
