from django.db import models
from .maps.google_maps import GoogleMaps

class Overlay(models.Model):
    GHG_OFFICE_LATITIUDE = 45.516750
    GHG_OFFICE_LONGTITUDE = -73.578500

    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longtitude = models.FloatField()

    def __str__(self):
        return "{} ({})".format(self.id, self.name)

    def url(self):
        return GoogleMaps().url(self.latitude, self.longtitude)