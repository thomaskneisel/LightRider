from Event import Event
from LightRider.Sequence import Sequence

class Disconnected(Event):
	def _initInstance(self):
		self.leds = [[24, 0]]

