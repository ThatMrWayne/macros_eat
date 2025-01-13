from django.urls import path
from food.views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('public-food/', get_public_food),
]

router = DefaultRouter()
router.register(r"my-food", FoodViewSet)
urlpatterns += router.urls