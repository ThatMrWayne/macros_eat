from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    weight = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'created_at'],
                name='unique_weight_user_created_at'
            )
        ]
