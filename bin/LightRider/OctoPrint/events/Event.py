from LightRider.Sequences import Sequence

class Event(object):
	def __init__(self):
		self.sequence = None
		self.leds = []

		self._initInstance()

	def _initInstance(self):
		speed = 0.2
                self.sequence = Sequence(speed, [[1,1,0,0,0,1,1,1,0,0,1,1,0],[0,1,1,1,0,0,0,1,1,0,0,1]])
                self.leds = [
                        [23, 1],
                        [24, 0],
                        [26, 1]
                ]
