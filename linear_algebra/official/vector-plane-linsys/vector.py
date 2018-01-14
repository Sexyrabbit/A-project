from decimal import Decimal

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.idx = 0

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __iter__(self):
        return self

    def next(self):
       self.idx += 1
       try:
           return Decimal(self.coordinates[self.idx-1])
       except IndexError:
           self.idx = 0
           raise StopIteration  # Done iterating.

    def __getitem__(self,index):
        return Decimal(self.coordinates[index])

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
