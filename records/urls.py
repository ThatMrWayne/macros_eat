from django.urls import path
from records.views import *


urlpatterns = [
    path('daily-record/', RecordViewSet.as_view(actions={
        "get": "retrieve"
    }))
]