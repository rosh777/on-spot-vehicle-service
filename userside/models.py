from django.db import models

class Vehicle(models.Model):
    vehicleType = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    fuel = models.CharField(max_length=25)

    def __str__(self):
        return self.brand

