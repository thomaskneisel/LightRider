from Event import Event
from LightRider.Sequences import Welcome
from LightRider.Sequences import Row

class Startup(Event):
	def _initInstance(self):
		self.leds = [[24, 1]] ## green led on
		sequence = Welcome()
		sequence.appendRow(Row(0.2,[0,0,0,0,0,0,0,0,0,0,0,0])) ## lights out :)
		self.sequence = sequence

	
	
