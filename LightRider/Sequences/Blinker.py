from Sequence import Sequence 
from Row import Row

class Blinker(Sequence):
	def __init__(self, speed=0.8):
		Sequence.__init__(
			self, [
				Row(speed, [1,1,1,1,1,1,0,0,0,0,0,0]),
				Row(speed, [0,0,0,0,0,0,1,1,1,1,1,1]),
				Row(0.001, [0,0,0,0,0,0,0,0,0,0,0,0]),
			],
			99
		)

