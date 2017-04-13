import unittest
import sys; sys.path.append('../')
from gpsimy.models import Command
from gpsimy.models import Event
from datetime import datetime


class TestCommand(unittest.TestCase):

	def setUp(self):
		pass

	def test_position(self):
		c = Command()
		c.position = (12.3123, 123.1234)
		self.assertIsNotNone(c)
		self.assertEqual(c.position, (12.3123, 123.1234, ))

	def test_event(self):
		now = datetime.utcnow()
		event = Event(timestamp=now)
		self.assertEquals(event.timestamp, now)


if __name__ == '__main__':
	unittest.main()