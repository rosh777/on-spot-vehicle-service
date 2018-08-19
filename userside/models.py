from django.contrib.gis import geos
from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models


class Vehicle(models.Model):
    vehicleType = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    fuel = models.CharField(max_length=25)

    def __str__(self):
        return self.brand

class Shop(models.Model):
    name = models.CharField(max_length=200, null= True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    location = models.PointField(geography=True, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.location = Point(self.long, self.lat)
        super(Shop, self).save(kwargs)

