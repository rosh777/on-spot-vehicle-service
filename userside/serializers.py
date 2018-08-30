from rest_framework import fields, serializers
from .models import Vehicle, Shop
from userside.models import SERVICE_CHOICES


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    distance = serializers.DecimalField(source='distance.km', max_digits=10,
                                        decimal_places=2, required=False,
                                        read_only=True)
    services = fields.MultipleChoiceField(choices=SERVICE_CHOICES)

    class Meta:
        model = Shop
        geo_field = "location"
        fields = ('id', 'logo', 'name', 'type', 'phone', 'services', 'address', 'city', 'lat', 'long', 'location', 'distance', 'isActive')



