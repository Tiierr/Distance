# -*- coding:utf-8 -*-
from .geo import Geo
from .antipodes import Antipodes

__all__ = ['Distance']


class Distance:
    def __init__(self, address):
        self.address = address

    def geo(self):
        return Geo(self.address)

    @property
    def status(self):
        return self.geo().status

    def lat(self):
        return self.geo().lat

    def lng(self):
        return self.geo().lng


    @property
    def latlng(self):
        return [float(self.lat()), float(self.lng())]

    @property
    def relatlng(self):
        return Antipodes(self.lat(), self.lng()).result_list

    @property
    def relatlng_str(self):
        return Antipodes(self.lat(), self.lng()).result_str
