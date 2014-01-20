from Event import Event
from LightRider.Sequences import Sequence

class Connected(Event):
	def _initInstance(self):
		self.leds = [[24, 1]]

