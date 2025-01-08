from django.urls import path
from authen.views import *


urlpatterns = [
    path('signup/', signup),
]
