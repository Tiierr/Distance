# -*- coding:utf-8 -*-
import json
import requests

from .exception import LcException
from config import keys

__all__ = ['GoogleGeo']

class GoogleGeo:
    def __init__(self, location):
        self._api = 'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(location, keys['GOOGLE_MAPS_PYTHON_KEY'])
        self._content = json.loads(requests.get(self._api).text)

    @property
    def content(self):
        return self._content

    @property
    def results(self):
        if self.status == 'OK':
            return self.content['results']
        raise LcException("The location is not exist.")

    @property
    def status(self):
        return self.content['status']

    @property
    def geometry(self):
        return self.results[0]['geometry']

    @property
    def latlng(self):
        return self.geometry['location']

    @property
    def lat(self):
        return float(self.latlng['lat'])

    @property
    def lng(self):
        return float(self.latlng['lng'])

    @property
    def latlng_list(self):
        return self.listToFloat([self.latlng['lat'], self.latlng['lng']])

    def listToFloat(self, lists):
        return list(map(float, lists))
