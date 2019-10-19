from django.core.files.uploadedfile import SimpleUploadedFile

import httpretty

from ..models import Overlay
from ..maps import google_maps

PLUME_FILE_FIXTURE = "test_fixtures/plume.png"
SATALLITE_MAP_FILE_FIXTURE = "test_fixtures/satallite_map_fixture.png"

# @httpretty.activate
def create_overlay(name, latitude=Overlay.GHG_OFFICE_LATITIUDE, longtitude=Overlay.GHG_OFFICE_LONGTITUDE, download_map=True):
    plume = SimpleUploadedFile(name=PLUME_FILE_FIXTURE, content=open(PLUME_FILE_FIXTURE, 'rb').read(), content_type='image/png')
    overlay = Overlay(
        name=name,
        latitude=latitude,
        longtitude=longtitude,
        plume=plume,
    )
    overlay.full_clean()

    if download_map:
        httpretty.enable()  # enable HTTPretty so that it will monkey patch the socket module
        httpretty.register_uri(
            httpretty.GET,
            google_maps.GoogleMaps.BASE_URL,
            body='{"origin": "127.0.0.1"}'
        )
        overlay.download_satellite_map_and_save()
        httpretty.disable()
        httpretty.reset()
    else:
        overlay.save()
    return overlay
