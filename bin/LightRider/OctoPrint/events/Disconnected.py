from Event import Event
from LightRider.Sequences import Sequence

class Disconnected(Event):
	def _initInstance(self):
		self.leds = [[24, 0]]

