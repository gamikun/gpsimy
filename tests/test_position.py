import unittest
import sys; sys.path.append('../')
from gpsimy.models import Position
from datetime import datetime


class TestPosition(unittest.TestCase):
    def test_latlng(self):
        pos = Position(29.923123, -111.012341)
        self.assertEquals(pos.lat, 29.923123)
        self.assertEquals(pos.lng, -111.012341)

    def test_lat(self):
        pos = Position(29.923123, None)
        self.assertEquals(pos.lat, 29.923123)
        self.assertIsNone(pos.lng)

    def test_lng(self):
        pos = Position(None, -111.012341)
        self.assertEquals(-111.012341, pos.lng)
        self.assertIsNone(pos.lat)


if __name__ == '__main__':
    unittest.main()
