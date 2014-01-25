from Event import Event
from LightRider.Sequences import Blinker

class Disconnected(Event):
	def _initInstance(self):
		self.leds = [[23, 0], [24, 1]]
		self.sequence = Blinker()

