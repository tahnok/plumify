from django.test import TestCase

from ..models import Overlay
from .factories import create_overlay

class OverlayTest(TestCase):
    def test_satallite_download_map_and_save(self):
        overlay = create_overlay("example", download_map=False)
        self.assertFalse(overlay.satallite_map)
        overlay.download_satellite_map_and_save()
        self.assertIsNotNone(overlay.satallite_map)