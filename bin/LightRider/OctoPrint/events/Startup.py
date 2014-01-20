from Event import Event
from LightRider.Sequences import Welcome

class Startup(Event):
	def _initInstance(self):
		self.leds = [[23, 1]]
		self.sequence = Welcome()

	
	
