from Event import Event
from LightRider.Sequence import Sequence

class Connected(Event):
	def _initInstance(self):
		self.leds = [[24, 1]]

