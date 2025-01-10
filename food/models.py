from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    food_name = models.TextField()
