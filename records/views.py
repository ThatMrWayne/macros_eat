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

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        update_data = request.data
        if instance.user_id != request.user.id:
            return Response({"success": False}, status=status.HTTP_403_FORBIDDEN)
        Record.objects.filter(pk=instance.id).update(**update_data)

        return Response({'ok': True}, status=status.HTTP_200_OK)


class IntakeViewSet(viewsets.GenericViewSet):
    queryset = Intakes.objects.all()
    serializer_class = IntakeSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        user = request.user
        data = request.data
        try:
            Record.objects.get(id=data["record_id"], user_id=user.id)
        except Record.DoesNotExist:
            return Response({"success": False}, status=status.HTTP_403_FORBIDDEN)

        new_intake = Intakes.objects.create(**data)
        serializer = self.get_serializer(new_intake)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        try:
            Record.objects.get(id=instance.record_id, user_id=request.user.id)
        except Record.DoesNotExist:
            return Response({"success": False}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)