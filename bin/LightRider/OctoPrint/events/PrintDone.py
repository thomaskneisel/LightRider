from Event import Event
from LightRider.Sequences import Circle

class PrintDone(Event):
	def _initInstance(self):
		self.leds = [[24,1], [23,1], [26,0]]
		self.sequence = Circle()
		self.sequence.repeat = 99
