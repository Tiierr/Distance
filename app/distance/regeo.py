# -*- coding:utf-8 -*-
import json
import requests

from config import keys

__all__ = ['Location', 'Address', 'AddressCompontent', 'Regeo']


class Location:
    def __init__(self, lat, lng):
        self._api = 'https://maps.googleapis.com/maps/api/geocode/json?language=zh-CN&latlng={0},{1}&key={2}'.format(lat, lng, keys['GOOGLE_MAPS_PYTHON_KEY'])
        self.content = json.loads(requests.get(self._api).text)

    @property
    def results(self):
        return self.content['results']

    @property
    def status(self):
        return self.content['status']

    @property
    def results_length(self):
        return len(self.results)

    # get a address
    def result_at(self, i):
        if i > self.results_length - 1:
            raise 'Index Error: index is not legal'
        return self.results[i]

class Address:
    def __init__(self, address):
        self.address = address

    @property
    def address_components(self):
        return self.address['address_components']

    @property
    def geometry(self):
        return self.address['geometry']

    @property
    def formatted_address(self):
        return self.address['formatted_address']

    @property
    def place_id(self):
        return self.address['place_id']

    @property
    def types(self):
        return self.address['types']

    @property
    def address_components_length(self):
        return len(self.address_components)

    # get a address component
    def address_component_at(self, i):
        if i > self.address_components_length - 1:
            raise 'Index Error: index is not legal'
        return self.address_components[i]


class AddressCompontent:
    def __init__(self, ac):
        self.ac = ac

    @property
    def long_name(self):
        return self.ac['long_name']

    @property
    def short_name(self):
        return self.ac['short_name']

    @property
    def types(self):
        return self.ac['types']

class Regeo:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    @property
    def location(self):
        return Location(self.lat, self.lng)

    @property
    def results(self):
        results = []
        for i in range(self.location.results_length):
            adr = []
            address = Address(self.location.result_at(i))
            for j in range(address.address_components_length):
                ac = AddressCompontent(address.address_component_at(j))
                if not self.is_number(ac.long_name) and ac.long_name not in adr:
                    adr.append(ac.long_name)
            results.append(adr)
        return results

    @property
    def results_str(self):
        results_str = []
        for i in range(len(self.results)):
            results_str.append(' '.join(self.results[i][::-1]))
        return results_str

    @property
    def first_result(self):
        return self.results_str[0]

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False
