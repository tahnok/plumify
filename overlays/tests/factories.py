from django.core.files.uploadedfile import SimpleUploadedFile
import httpretty

from ..models import Overlay
from ..maps import google_maps

PLUME_FILE_FIXTURE = "test_fixtures/plume.png"
SATALLITE_MAP_FILE_FIXTURE = "test_fixtures/satallite_map_fixture.png"

def create_overlay(name, latitude=Overlay.GHG_OFFICE_LATITIUDE, longtitude=Overlay.GHG_OFFICE_LONGTITUDE, process=True):
    plume = SimpleUploadedFile(name=PLUME_FILE_FIXTURE, content=open(PLUME_FILE_FIXTURE, 'rb').read(), content_type='image/png')
    overlay = Overlay(
        name=name,
        latitude=latitude,
        longtitude=longtitude,
        plume=plume,
    )
    overlay.full_clean()

    if process:
        httpretty.enable()  # enable HTTPretty so that it will monkey patch the socket module
        httpretty.register_uri(
            httpretty.GET,
            google_maps.GoogleMaps.BASE_URL,
            body= _satallite_map_contents()
        )
        overlay.process_and_save()
        httpretty.disable()
        httpretty.reset()
    else:
        overlay.save()
    return overlay

def _satallite_map_contents():
    return open(SATALLITE_MAP_FILE_FIXTURE, 'rb').read()