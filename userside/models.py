from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models
from multiselectfield import MultiSelectField


class Vehicle(models.Model):
    vehicleType = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    fuel = models.CharField(max_length=25)

    def __str__(self):
        return self.brand


SERVICE_CHOICES = (('A battery test checking','A battery test checking'),
                   ('The tyres and their pressure','The tyres and their pressure'),
                   ('Visual inspection of steering and suspension','Visual inspection of steering and suspension'),
                   ('Check antifreeze/engine coolant','Check antifreeze/engine coolant'),
                   ('Top up fluid levels and washers', 'Top up fluid levels and washers'),
                   ('Check lights', 'Check lights'))

class Shop(models.Model):
    logo = models.CharField(max_length= 500, null=True, blank=True)
    name = models.CharField(max_length=200, null= True)
    type = models.CharField(max_length=100, null=True, default='Vehicle Service Station')
    services = MultiSelectField(choices=SERVICE_CHOICES, null=True)
    phone = models.CharField(max_length=13, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    location = models.PointField(srid=4326, geography=True, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        self.location = Point(self.long, self.lat)
        super(Shop, self).save(kwargs)

