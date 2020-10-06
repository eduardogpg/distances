from math import atan2
from math import cos
from math import radians
from math import sin
from math import sqrt


class Distance:
    def calculate_distance(
        self,
        lat1: float,
        long1: float,
        lat2: float,
        long2: float
    ) -> float:

        (lat1, long1) = radians(lat1), radians(long1)
        (lat2, long2) = radians(lat2), radians(long2)

        dlon: float = long2 - long1
        dlat: float = lat2 - lat1

        a: float = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c: float = 2 * atan2(sqrt(a), sqrt(1 - a))

        return 6373.0 * c
