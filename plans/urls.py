from django.urls import path
from plans.views import *
from rest_framework.routers import DefaultRouter


urlpatterns = []

router = DefaultRouter()
router.register(r"diet-plan", PlanViewSet)
urlpatterns += router.urls