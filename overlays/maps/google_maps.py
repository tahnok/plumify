from urllib.parse import urlencode

import secrets

class GoogleMaps:
    BASE_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
    WIDTH = 514 # width of sample image
    HEIGHT = 257 # height of sample plume image
    # TODO fix zoom to be accurate to 10km x 5km
    # https://gis.stackexchange.com/questions/7430/what-ratio-scales-do-google-maps-zoom-levels-correspond-to
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
