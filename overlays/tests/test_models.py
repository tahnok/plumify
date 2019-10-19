from django.test import TestCase

from ..models import Overlay
from .factories import create_overlay

class OverlayTest(TestCase):
    def test_satallite_download_map_and_save(self):
        overlay = create_overlay("example", process=False)
        self.assertFalse(overlay.satallite_map)

        overlay.download_satellite_map_and_save()

        self.assertIsNotNone(overlay.satallite_map)

    def test_generate_plume_on_satallite_map(self):
        overlay = create_overlay("example", process=False)
        overlay.download_satellite_map_and_save()
        self.assertFalse(overlay.plume_on_satallite_map)

        overlay.generate_plume_on_satallite_map()

        self.assertIsNotNone(overlay.plume_on_satallite_map)

    def test_process_and_save(self):
        overlay = create_overlay("example", process=False)
        self.assertFalse(overlay.satallite_map)
        self.assertFalse(overlay.plume_on_satallite_map)

        overlay.process_and_save()

        self.assertIsNotNone(overlay.plume_on_satallite_map)
        self.assertIsNotNone(overlay.satallite_map)