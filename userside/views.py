from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Vehicle
from .serializers import VehicleSerializer

# List all vehicles or create one
# vehicles/
class Vehicle(viewsets.ModelViewSet):

    # def get(self, request):
    #     vehicles = Vehicle.objects.all()
    #     serializer = VehicleSerializer(vehicles, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


