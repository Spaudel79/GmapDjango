from ..models import Location
from .serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class LocationView(APIView):
    permission_classes = [IsAuthenticated]

    # pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):

        queryset = Location.objects.all().order_by("name")
        serializer = LocationSerializer(queryset,many=True)
        return Response(serializer.data,status=200)



