from Event import Event
from LightRider.Sequences import Clock

class Home(Event):
	def _initInstance(self):
		self.leds = [[24,1], [23,1]]
		self.sequence = Clock()
