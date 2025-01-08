from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from authen.models import UserProfile
from authen.decorators import *
from authen.utils import CsrfExemptSessionAuthentication
from datetime import datetime, timezone

User = get_user_model()


@api_view(['POST']) # only csrf_exempt in DRF APIview if not SessionAuthentication
@set_custom_attr("authentication_classes", [CsrfExemptSessionAuthentication])
def signup(request):
    signup_data = request.data
    email = signup_data.get('email', None)
    name = signup_data.get('name', None)
    password = signup_data.get('password', None)
    identity = signup_data.get('identity', None)
    print(signup_data)
    local_dt = datetime.now()
    utc_dt = local_dt.astimezone(timezone.utc)
    if not all([email, name, password, identity]):
        response = Response({'error': True}, status=status.HTTP_400_BAD_REQUEST)
    elif UserProfile.objects.filter(email=email).exists() or \
        User.objects.filter(username=name).exists():
        response = Response({'error': True, 'msg': 'email or username already  exists'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user = User.objects.create_user(username=name, password=password, date_joined=utc_dt)
        UserProfile.objects.create(user=user, identity=identity, email=email)
        response = Response({'status':'ok'}, status=status.HTTP_201_CREATED)
    return response
