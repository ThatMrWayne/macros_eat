from django.urls import path
from weight.views import *


urlpatterns = [
    path("my-weight/", WeightViewSet.as_view(actions={
        "patch": "partial_update",
        "get": "list",
        "post": "create"
    }))
]
