from Sequence import Sequence
from Row import Row

class Orbit(Sequence):
	def __init__(self, speed=0.03):
		Sequence.__init__(
			self, [
				Row(speed, [1,0,0,0,0,0,1,0,0,0,0,0]),
				Row(speed, [0,1,0,0,0,0,0,1,0,0,0,0]),
				Row(speed, [0,0,1,0,0,0,0,0,1,0,0,0]),
				Row(speed, [0,0,0,1,0,0,0,0,0,1,0,0]),
				Row(speed, [0,0,0,0,1,0,0,0,0,0,1,0]),
				Row(speed, [0,0,0,0,0,1,0,0,0,0,0,1]),				
			],
			12
		)
