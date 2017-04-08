# -*- coding:utf-8 -*-
from .google_geo import GoogleGeo
from .antipodes import Antipodes

__all__ = ['Distance']

class GoogleDistance:
    def __init__(self, address):
        self.address = address

    def geo(self):
        return GoogleGeo(self.address)

    @property
    def status(self):
        return self.geo().status

    def lat(self):
        return self.geo().lat

    def lng(self):
        return self.geo().lng

    @property
    def latlng(self):
        return self.geo().latlng_list

    @property
    def relatlng(self):
        return Antipodes(self.lat(), self.lng()).result_list

    @property
    def relatlng_str(self):
        return Antipodes(self.lat(), self.lng()).result_str
