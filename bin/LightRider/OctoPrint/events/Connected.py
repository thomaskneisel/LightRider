from Event import Event

class Connected(Event):
	def _initInstance(self):
		self.leds = [[23, 1], [24, 1]]

