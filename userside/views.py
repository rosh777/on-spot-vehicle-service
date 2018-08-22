
from rest_framework import viewsets
from .models import Vehicle, Shop
from .serializers import VehicleSerializer, ShopSerializer
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry

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

class Shop(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        latitude = self.request.query_params.get('lat', None)
        longitude = self.request.query_params.get('lng', None)

        if latitude and longitude:
            pnt = GEOSGeometry('POINT(' + str(longitude) + ' ' + str(latitude) + ')', srid=4326)
            qs = qs.annotate(distance= Distance('location', pnt)).order_by('distance')
        return qs

