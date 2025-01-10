from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Plan(models.Model):
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fat = models.IntegerField()
    plan_calories = models.IntegerField()
    plan_name = models.TextField()
