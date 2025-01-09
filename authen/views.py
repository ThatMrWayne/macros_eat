from django.contrib import auth
from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from authen.models import UserProfile
from authen.decorators import *
from datetime import datetime, timezone
from utils.exceptions import *

User = get_user_model()


@api_view(['POST']) # SessionAuthentication enforce csrf on authenticated user
def signup(request):
    signup_data = request.data
    email = signup_data.get('email', None)
    name = signup_data.get('name', None)
    password = signup_data.get('password', None)
    identity = signup_data.get('identity', None)
    local_dt = datetime.now()
    utc_dt = local_dt.astimezone(timezone.utc)
    if not all([email, name, password, identity]):
        return MissingInputError("Please provide complete info")()
    else:
        try:
            user = User.objects.create_user(username=name, password=password, email=email ,date_joined=utc_dt)
            UserProfile.objects.create(user=user, identity=identity)
        except IntegrityError:
            return AlreadyExistError("username or email already exist.")()
    return Response({'status':'ok'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def signin(request):
    signin_data = request.data
    email = signin_data.get('email', None)
    password = signin_data.get('password', None)
    identity = signin_data.get("identity", None)
    user = None
    if not all([email, password, identity]):
        return MissingInputError("Please provide complete info")()
    else:
        user = auth.authenticate(email=email, password=password)

    if user is None:
        return ObjectNotExistError("User does not exist.")()

    user_profile = user.userprofile
    auth.login(request, user)
    return Response({'initial': user_profile.first_login}, status=status.HTTP_200_OK)
