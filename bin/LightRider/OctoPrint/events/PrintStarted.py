from Event import Event
from LightRider.Sequences import AllOn

class PrintStarted(Event):
	def _initInstance(self):
		self.leds = [[24,1], [23,1], [26,1]]
		self.sequence = AllOn()

