from django.db import models

class FuelStation(models.Model):
    opis_id = models.CharField(max_length=100, null=True, blank=True)
    truckstop_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    retail_price = models.FloatField()

    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self):
        return self.truckstop_name# Create your models here.
