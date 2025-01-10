from rest_framework import serializers
from authen.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    identity = serializers.SerializerMethodField()
    initial = serializers.SerializerMethodField()

    def get_identity(self, instance):
        identity_map = {
            "general_user": 1,
            "nutritionist": 2
        }
        return identity_map[instance.identity]

    def get_initial(self, instance):
        return instance.first_login

    class Meta:
        model = UserProfile
        fields = (
            "id",
            "identity",
            "initial"
        )
