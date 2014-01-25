from Event import Event
from LightRider.Sequences import Blinker

class Paused(Event):
	def _initInstance(self):
		self.leds = [[24,1], [23,1], [26,1]]
		self.sequence = Blinker()
