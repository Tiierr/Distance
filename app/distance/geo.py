import requests
import json

from config import keys
from .exception import LcException

__all__ = ['Geo']

class Geo:
    def __init__(self, address):
        self.address = address

    def address_api(self, address):
        return 'http://restapi.amap.com/v3/geocode/geo?address={0} \
                &output=JSON&key={1}'.format(address,keys['GAODE_MAPS_PYTHON_KEY'])

    @property
    def api(self):
        return self.address_api(self.address)

    @property
    def content(self):
        return json.loads(requests.get(self.api).text)

    @property
    def geocodes(self):
        return self.content['geocodes']

    @property
    def count(self):
        return self.content['count']

    @property
    def status(self):
        if self.count == '0':
            return '404'
        return '200'

    @property
    def geocode(self):
        if self.status == '404':
            raise LcException("The location is not exist.")

        return self.geocodes[0]

    def can(self):
        return 'location' in self.geocode

    @property
    def location(self):
        if self.can():
            return self.geocode['location']
        raise LcException("The location is out of the Gaode Map's range.")

    def coord(self):
        return self.location.split(',')

    @property
    def lng(self):
        return self.coord()[0]

    @property
    def lat(self):
        return self.coord()[1]
