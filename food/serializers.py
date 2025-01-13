from rest_framework import serializers
from food.models import *


class FoodSerializer(serializers.ModelSerializer):
    food_id = serializers.SerializerMethodField()

    def get_food_id(self, instance):
        return instance.id

    class Meta:
        model = Food
        fields = (
            "food_id",
            "food_name",
            "protein",
            "carbs",
            "fat",
        )
