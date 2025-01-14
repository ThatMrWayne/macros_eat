from rest_framework import serializers
from weight.models import *


class WeightSerializer(serializers.ModelSerializer):
    create_at = serializers.SerializerMethodField()

    def get_create_at(self, instance):
        # history reason , return utc millisec timestamp
        return int(instance.created_at.timestamp()*1000)

    class Meta:
        model = Weight
        fields = (
            "create_at",
            "weight",
        )
