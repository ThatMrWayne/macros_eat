from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class GenderType(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"


class IdentityType(models.TextChoices):
    GENERAL_USER = "general_user"
    NUTRITIONIST = "nutritionist"


# Create your models here.
class UserProfile(models.Model):
    identity = models.TextField(choices=[(v, v.value) for v in IdentityType])
    sex = models.CharField(max_length=8, choices=[(v, v.value) for v in GenderType])
    first_login = models.BooleanField(default=True)
    habit = models.IntegerField(blank=True, null=True)
    target = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField(unique=True)
