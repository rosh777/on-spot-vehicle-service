from django.db import models

class Vehicle(models.Model):
    vehicleType_choices = (('bike', 'Bike'), ('car', 'Car'), ('truck', 'Truck'), ('bus', 'Bus'), ('autorickshaw', 'Autorickshaw'))
    vehicleType = models.CharField(max_length=25, choices=vehicleType_choices, default='car')
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    fuel_choices = (('petrol', 'Petrol'),('diesel', 'Diesel'))
    fuel = models.CharField(max_length=6, choices=fuel_choices, default='diesel',)

    def __str__(self):
        return self.brand

