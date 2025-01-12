from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fat = models.IntegerField()
    plan_calories = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'created_at'],
                name='unique_user_created_at'
            )
        ]


class Intakes(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    food_name = models.TextField()
    amount = models.FloatField()
