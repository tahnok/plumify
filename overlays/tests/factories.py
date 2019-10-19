from django.core.files.uploadedfile import SimpleUploadedFile


from ..models import Overlay

PLUME_FILE_FIXTURE = "test_fixtures/plume.png"

def create_overlay(name, latitude=Overlay.GHG_OFFICE_LATITIUDE, longtitude=Overlay.GHG_OFFICE_LONGTITUDE):
    plume = SimpleUploadedFile(name=PLUME_FILE_FIXTURE, content=open(PLUME_FILE_FIXTURE, 'rb').read(), content_type='image/png')
    overlay = Overlay(
        name=name,
        latitude=latitude,
        longtitude=longtitude,
        plume=plume,
    )
    overlay.full_clean()

    overlay.save()
    return overlay
