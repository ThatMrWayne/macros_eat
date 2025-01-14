from django.urls import path
from weight.views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("my-weight/", WeightViewSet.as_view(actions={
        "patch": "partial_update",
        "get": "list",
        "post": "create"
    }))
]
