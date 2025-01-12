from django.forms.models import model_to_dict
from rest_framework import serializers
from records.models import *


class IntakeSerializer(serializers.ModelSerializer):
    intake_id = serializers.SerializerMethodField()

    def get_intake_id(self, instance):
        return instance.id

    class Meta:
        model = Intakes
        fields = (
            "intake_id",
            "food_name",
            "protein",
            "carbs",
            "fat",
            "amount"
        )


class RecordSerializer(serializers.ModelSerializer):
    food_record = serializers.SerializerMethodField()
    day_record = serializers.SerializerMethodField()

    def get_day_record(self, instance):
        result = model_to_dict(instance)
        del result["created_at"]
        result["record_id"] = result["id"]
        del result["id"]
        return result

    def get_food_record(self, instance):
        record_id = instance.id
        intakes_query = Intakes.objects.filter(record_id=record_id)
        intakes_data = IntakeSerializer(intakes_query, many=True).data
        return intakes_data

    class Meta:
        model = Record
        fields = (
            "day_record",
            "food_record"
        )
