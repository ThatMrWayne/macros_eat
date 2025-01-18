from django.urls import path
from authen.views import *


urlpatterns = [
    path('signup/', signup),
    path('signin/', signin),
    path('signout/', signout),
    path('user/', UserViewSet.as_view(actions={
        "patch": "partial_update",
        "get": "retrieve"
    }))
]
