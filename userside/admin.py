from django.contrib import admin
from .models import Vehicle, Shop
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Vehicle)
admin.site.register(Shop, LeafletGeoAdmin)


