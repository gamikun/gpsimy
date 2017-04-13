import unittest
import sys; sys.path.append('../')
from gpsimy.models import Command
from gpsimy.models import Event, InputChanged
from datetime import datetime


class TestEvents(unittest.TestCase):

	def setUp(self):
		pass

	def test_event(self):
		now = datetime.utcnow()
		event = Event(timestamp=now)
		self.assertEquals(event.timestamp, now)

	def test_input_evnt(self):
		now = datetime.utcnow()
		event = 


if __name__ == '__main__':
	unittest.main()