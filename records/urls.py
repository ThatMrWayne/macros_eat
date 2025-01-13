from rest_framework.routers import DefaultRouter
from django.urls import path
from records.views import *


urlpatterns = [
    path("daily-record/", RecordViewSet.as_view(actions={
        "get": "retrieve",
        "post": "create",
    })),
    path("daily-record/<int:pk>/", RecordViewSet.as_view(actions={
        "patch": "partial_update"
    }))
]

router = DefaultRouter()
router.register(r"record-intake", IntakeViewSet)
urlpatterns += router.urls
