import requests
import uuid
import tempfile

from django.core import files
from django.db import models

from .maps.google_maps import GoogleMaps

def plume_path(instance, filename):
    return 'plumes/{}_{}.png'.format(instance.name, uuid.uuid4())

def satallite_map_path(instance, filename):
    return 'sat_maps/{}_{}.png'.format(instance.name, uuid.uuid4())


class Overlay(models.Model):
    GHG_OFFICE_LATITIUDE = 45.516750
    GHG_OFFICE_LONGTITUDE = -73.578500

    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    plume = models.ImageField(upload_to=plume_path)
    satallite_map = models.ImageField(upload_to=satallite_map_path, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.id, self.name)

    def download_satellite_map_and_save(self):
        response = requests.get(self.satellite_map_url(), allow_redirects=True, stream=True)
        if response.status_code != requests.codes.ok:
            raise Exception("Unable to download satallite image")
        temp_file = tempfile.NamedTemporaryFile()
        for block in response.iter_content(1024 * 8):
            if not block:
                break
            temp_file.write(block)
        self.satallite_map.save("test.png", files.File(temp_file))

    def satellite_map_url(self):
        return GoogleMaps().url(self.latitude, self.longtitude)
