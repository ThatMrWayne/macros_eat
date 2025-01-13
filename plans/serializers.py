from rest_framework import serializers
from plans.models import *


class PlanSerializer(serializers.ModelSerializer):
    plan_id = serializers.SerializerMethodField()

    def get_plan_id(self, instance):
        return instance.id


    class Meta:
        model = Plan
        fields = (
            "plan_id",
            "plan_name",
            "protein",
            "carbs",
            "fat",
            "plan_calories"
        )
