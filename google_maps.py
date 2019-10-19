from urllib.parse import urlencode

import secrets

class GoogleMaps:
    BASE_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
    WIDTH = 400
    HEIGHT = 400

    def url(self, latitude, longtitude):
        params = {
            'center': "{},{}".format(latitude, longtitude),
            'zoom': 15,
            'size': "{}x{}".format(self.WIDTH, self.HEIGHT),
            'maptype': 'satellite',
            'key': secrets.GOOGLE_API_KEY,
        }

        return self.BASE_URL + urlencode(params)
