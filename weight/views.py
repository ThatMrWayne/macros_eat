from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from weight.serializers import *
from weight.models import *
from utils.utils import convert_timestamp_to_utc_datetime
from utils.exceptions import *


# Create your views here.
class WeightViewSet(viewsets.GenericViewSet):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = request.user
        start_date = request.query_params.get("sdate", None)
        end_date = request.query_params.get("edate", None)
        if not all([start_date, end_date]):
            return MissingInputError("Please provide start date and end date")()

        start_date = convert_timestamp_to_utc_datetime(start_date)
        end_date = convert_timestamp_to_utc_datetime(end_date)

        if (end_date - start_date).days > 90:
            return WrongInputError("Please select day range less than or equal to 90 days")()

        qs = self.queryset.filter(user_id=user.id, created_at__range=(start_date, end_date)).order_by("created_at")
        serializer = self.get_serializer(qs, many=True)
        payload = serializer.data
        data = {"weight_record": payload}

        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        user = request.user
        data = request.data
        data["user_id"] = user.id
        data["created_at"] = convert_timestamp_to_utc_datetime(data["created_at"])
        try:
            Weight.objects.create(**data)
        except IntegrityError:
            return AlreadyExistError("Weight on today already exist")()

        return Response({"success": True}, status=status.HTTP_201_CREATED)

    def partial_update(self, request):
        user = request.user
        data = request.data
        target_date = convert_timestamp_to_utc_datetime(data["created_at"])
        try:
            Weight.objects.filter(user_id=user.id, created_at=target_date).\
                update(weight=data["new_weight"])
        except Weight.DoesNotExist:
            return ObjectNotExistError("Weight for today does not exist")()

        return Response({"success": True}, status=status.HTTP_200_OK)
