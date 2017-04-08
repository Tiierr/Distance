from werkzeug.routing import BaseConverter

__all__ = ['ListConverter', 'ListToString']

class ListConverter(BaseConverter):

    def to_python(self, value):
        return list(map(float, value.split(',')))

    def to_url(self, values):
        return ','.join(super(ListConverter, self).to_url(value)
                            for value in values)

class ListToString(object):
    def __init__(self, lists):
        self.lists = lists

    def toString(self):
        return 'lat: {lat}, lng: {lng}'.format(lat=self.lists[0], lng=self.lists[1])
