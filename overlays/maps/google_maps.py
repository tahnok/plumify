from urllib.parse import urlencode

import secrets

class GoogleMaps:
    BASE_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
    WIDTH = 400
    HEIGHT = 400
    ZOOM = 15
    MAP_TYPE = 'satellite'

    def __init__(self, key=secrets.GOOGLE_API_KEY):
        self.key = key

    def url(self, latitude, longtitude):
        params = {
            'center': "{},{}".format(latitude, longtitude),
            'zoom': self.ZOOM,
            'size': "{}x{}".format(self.WIDTH, self.HEIGHT),
            'maptype': self.MAP_TYPE,
            'key': self.key,
        }

        return self.BASE_URL + urlencode(params)
