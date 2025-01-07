from django.urls import path
from authen.views import *


urlpatterns = [
    path('hello/', hello_world),
]