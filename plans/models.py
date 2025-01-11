from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


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

    @staticmethod
    def calc_plan(input: dict): #計算推薦飲食function
        bmr =(10 * round(input["weight"],1)) + (6.25 * round(input["height"],1)) - (5 * input["age"])
        if input["gender"] == "female":
            bmr = bmr - 161
        elif input["gender"] == "male":
            bmr = bmr + 5
        pal = {
            "sedentary":1.2,
            "light_activity":1.375,
            "moderate_activity":1.55,
            "very_active":1.725
        }
        calo_degree = {
            "lose_weight":0.8,
            "maintain":1,
            "gain_weight":1.2
        }
        tdee = bmr * pal[input["habit"]]
        calos = int(tdee * calo_degree[input["target"]])
        create_at = timezone.now()
        plan_name = "Recommended plan by system"
        recommended = {
                        "plan_name": plan_name,
                        "created_at": create_at,
                        "plan_calories": calos,
                        "protein": 40,
                        "fat": 30,
                        "carbs":30
                        }
        return recommended
