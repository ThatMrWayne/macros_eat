from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from records.models import *
from records.serializers import *
from utils.utils import convert_timestamp_to_utc_datetime


# Create your views here.
class RecordViewSet(viewsets.GenericViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, pk=None):
        user = request.user
        utc_datetime = convert_timestamp_to_utc_datetime(self.request.query_params.get('datetime'))
        try:
            instance = Record.objects.get(user=user, created_at=utc_datetime)
        except Record.DoesNotExist:
            instance = None
        data = self.get_serializer(instance).data if instance else {}
        payload = Response(data, status=status.HTTP_200_OK)
        return payload

    def create(self, request):
        user = request.user
        data = request.data
        data["created_at"] = convert_timestamp_to_utc_datetime(data["created_at"])
        data["user_id"] = user.id
        Record.objects.create(**data)
        return Response({"success": True}, status=status.HTTP_201_CREATED)
