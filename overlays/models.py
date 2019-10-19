from django.db import models

class Overlay(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(null=True)
    longtitude = models.FloatField(null=True)