from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from food.serializers import *


# Create your views here.
class FoodViewSet(viewsets.GenericViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        user = request.user
        qs = self.queryset.filter(user_id=user.id).order_by("-id")
        last_item_pk = int(request.query_params.get("last_item_pk", 0))
        if last_item_pk != 0: # 0 means from start (history reason use 0)
            qs = qs.filter(Q(id__lt=last_item_pk))
        serializer = self.get_serializer(qs[:10], many=True)
        payload = serializer.data
        last_item_pk = payload[-1]["food_id"] if payload else None
        data = {"data": payload, "last_item_pk": last_item_pk}

        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        user = request.user
        data = request.data
        data["user_id"] = user.id
        Food.objects.create(**data)
        return Response({"success": True}, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        if instance.user_id != request.user.id:
            return Response({"success": False}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_public_food(request):
    page_number = request.query_params.get("page", None)
    keyword = request.query_params.get("keyword", "")

    if keyword in (None, "") or page_number is None:
        return Response({"data": [], "nextPage": None}, status=status.HTTP_200_OK)
    page_number = int(page_number)
    result = Food.search_food(keyword, page_number)
    if result:
        next_page = page_number + 1
    else:
        next_page = None
    return Response({"data": result, "nextPage": next_page}, status=status.HTTP_200_OK)
