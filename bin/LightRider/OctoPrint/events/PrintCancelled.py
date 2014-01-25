from Event import Event
from LightRider.Sequences import Blinker

class PrintCancelled(Event):
	def _initInstance(self):
		self.leds = [[24,1], [23,1], [26,0]]
		self.sequence = Blinker()
