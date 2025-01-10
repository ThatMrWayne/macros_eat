from django.urls import path
from rest_framework.routers import DefaultRouter
from authen.views import *


urlpatterns = [
    path('signup/', signup),
    path('signin/', signin),
    path('user/', UserViewSet.as_view(actions={
        "patch": "partial_update",
        "get": "retrieve"
    }))
]
