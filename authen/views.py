from django.contrib import auth
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from authen.models import UserProfile
from authen.decorators import *
from django.utils import timezone
from utils.exceptions import *
from authen.serializers import UserProfileSerializer
from plans.models import *

User = get_user_model()


@api_view(['POST']) # SessionAuthentication enforce csrf on authenticated user
def signup(request):
    signup_data = request.data
    email = signup_data.get('email', None)
    name = signup_data.get('name', None)
    password = signup_data.get('password', None)
    identity = signup_data.get('identity', None)
    utc_dt = timezone.now()
    if not all([email, name, password, identity]):
        return MissingInputError("Please provide complete info")()
    else:
        try:
            user = User.objects.create_user(username=name, password=password, email=email ,date_joined=utc_dt)
            UserProfile.objects.create(user=user, identity=identity, name=name)
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


@api_view(['POST'])
def signout(request):
    response = redirect("home")
    response.delete_cookie("csrftoken")
    auth.logout(request)

    return response


class UserViewSet(viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, pk=None):
        instance = request.user.userprofile
        serializer = self.get_serializer(instance)
        payload = Response({"data": serializer.data}, status=status.HTTP_200_OK)
        return payload

    def partial_update(self, request, *args, **kwargs):
        update_data = request.data
        user = request.user
        user_profile = user.userprofile
        labels = ["gender","height","weight","habit","target","age",]
        habit_map = {
            1: "sedentary",
            2: "light_activity",
            3: "moderate_activity",
            4: "very_active"
        }
        target_map = {
            1: "lose_weight",
            2: "maintain",
            3: "gain_weight"
        }
        gender_map = {
            1: "male",
            2: "female"
        }
        final_data = {}
        for label in labels:
            if label == "habit":
                data = habit_map[update_data.get(label)]
            elif label == "target":
                data = target_map[update_data.get(label)]
            elif label == "gender":
                data = gender_map[update_data.get(label)]
            else:
                data = update_data.get(label)
            final_data[label] = data
        UserProfile.objects.filter(pk=user_profile.id).\
            update(first_login=False, **final_data)
        #calculate recommended plan and insert in db
        recommended_plan = Plan.calc_plan(final_data)
        recommended_plan["user_id"] = user.id
        Plan.objects.create(**recommended_plan)
        # historical reason: set `remind` in cookie for frontend to decide
        # whether show complete record page
        response = Response({'ok': True}, status=status.HTTP_200_OK)
        response.set_cookie(
            key="remind", # represent this user has execute filling out the first time form
            value="yes",
            secure=False, #for dev
            httponly=True,
        )
        return response
