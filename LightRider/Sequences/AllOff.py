from Sequence import Sequence 
from Row import Row

class AllOff(Sequence):
	def __init__(self, speed=1):
		Sequence.__init__(
			self, [
				Row(speed, [0,0,0,0,0,0,0,0,0,0,0,0]),
			],
			1
		)

