from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class GenderType(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"


class IdentityType(models.TextChoices):
    GENERAL_USER = "general_user"
    NUTRITIONIST = "nutritionist"


class ActivityLevelType(models.TextChoices):
    SEDENTARY = "sedentary"
    LIGHT_ACTIVITY = "light_activity"
    MODERATE_ACTIVITY = "moderate_activity"
    VERY_ACTIVE = "very_active"


class TargetType(models.TextChoices):
    LOSE_WEIGHT = "lose_weight"
    MAINTAIN = "maintain"
    GAIN_WEIGHT = "gain_weight"


# Create your models here.
class UserProfile(models.Model):
    identity = models.TextField(choices=[(v, v.value) for v in IdentityType])
    gender = models.CharField(max_length=8, choices=[(v, v.value) for v in GenderType])
    first_login = models.BooleanField(default=True)
    habit = models.TextField(choices=[(v, v.value) for v in ActivityLevelType])
    target = models.TextField(choices=[(v, v.value) for v in TargetType])
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    age = models.IntegerField(null=True)
