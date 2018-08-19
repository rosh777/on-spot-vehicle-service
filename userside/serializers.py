from rest_framework import serializers
from .models import Vehicle, Shop
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        #geo_field = "location"
        #fields = ('id', 'name', 'address', 'city', 'location')
        fields = '__all__'


