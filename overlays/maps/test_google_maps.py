import unittest
from urllib.parse import urlparse, parse_qs

from .google_maps import GoogleMaps

class TestGoogleMaps(unittest.TestCase):
    def test_generate_url(self):
        maps = GoogleMaps(key="test")
        generated_url = urlparse(maps.url(45.0, 20.0))
        expected_url = urlparse("https://maps.googleapis.com/maps/api/staticmap?zoom=12&size=514x257&maptype=satellite&center=45.0%2C20.0&key=test")
        self.assertEquals(expected_url.hostname, generated_url.hostname)
        self.assertEquals(expected_url.path, generated_url.path)
        self.assertEquals(parse_qs(expected_url.query), parse_qs(generated_url.query))