from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from plans.models import *
from plans.serializers import *


# Create your views here.
class PlanViewSet(viewsets.GenericViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = request.user
        qs = self.queryset.filter(user_id=user.id).order_by("-id")
        last_item_pk = int(request.query_params.get("last_item_pk", 0))
        if last_item_pk != 0: # 0 means from start (history reason use 0)
            qs = qs.filter(Q(id__lt=last_item_pk))
        serializer = self.get_serializer(qs[:10], many=True)
        payload = serializer.data
        last_item_pk = payload[-1]["plan_id"] if payload else None
        data = {"plans": payload, "last_item_pk": last_item_pk}

        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        user = request.user
        data = request.data
        data["user_id"] = user.id
        plan = Plan.objects.create(**data)
        plan.plan_name = f"Plan-{plan.id}"
        plan.save(update_fields=["plan_name"])
        return Response({"success": True}, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        if instance.user_id != request.user.id:
            return Response({"success": False}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
