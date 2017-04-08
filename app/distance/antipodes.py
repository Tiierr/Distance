__all__ = ['Antipodes']

class Antipodes:
    def __init__(self, lat, lng):
        self.lat = float(lat)
        self.lng = float(lng)

    def anti_latitude(self):
        return -self.lat

    def anti_longitude(self):
        if self.lng > 0:
            return self.lng - 180
        else:
            return 180 + self.lng

    @property
    def anti_lng(self):
        return self.anti_longitude()

    @property
    def anti_lat(self):
        return self.anti_latitude()

    @property
    def result(self):
        return (self.anti_lat, self.anti_lng)

    @property
    def result_list(self):
        return [self.anti_lat, self.anti_lng]

    @property
    def result_str(self):
        return str(self.anti_lat)  + ',' + str(self.anti_lng)

    @property
    def result_dict(self):
        return {'lat': self.anti_lat, 'lng': self.anti_lng}
