from urllib.parse import urlencode

import math
import secrets

class GoogleMaps:
    BASE_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
    REAL_WITH_KM = 10
    REAL_HEIGHT_KM = 5
    WIDTH = 514 # width of sample image
    HEIGHT = 257 # height of sample plume image
    MAP_TYPE = 'satellite'

    def __init__(self, key=secrets.GOOGLE_API_KEY):
        self.key = key

    def url(self, latitude, longtitude):
        params = {
            'center': "{},{}".format(latitude, longtitude),
            'zoom': self.zoom(self.WIDTH, self.REAL_WITH_KM, latitude),
            'size': "{}x{}".format(self.WIDTH, self.HEIGHT),
            'maptype': self.MAP_TYPE,
            'key': self.key,
        }

        return self.BASE_URL + urlencode(params)

    def zoom(self, image_width, real_width_km, latitude):
        """
        Calculate the appropriate zoom level for a given latitude according to:
        https://gis.stackexchange.com/questions/7430/what-ratio-scales-do-google-maps-zoom-levels-correspond-to

        image_width is in pixels

        real_width_km is in km

        latitiude is a floating point number

        metersPerPx = 156543.03392 * Math.cos(latLng.lat() * Math.PI / 180) / Math.pow(2, zoom)
        """
        meters_per_pixel = (real_width_km * 1000.0) / image_width 

        zoom = math.log2((156543.0339 * math.cos(latitude * math.pi / 180)) / meters_per_pixel)

        return int(round(zoom))