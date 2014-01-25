from Event import Event

class PrintFailed(Event):
	def _initInstance(self):
		self.leds = [[24,1], [23,1], [26,0]]
