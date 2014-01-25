from Sequence import Sequence 
from Row import Row

class Christmas(Sequence):
	def __init__(self, speed=0.85):
		Sequence.__init__(
			self, [
				Row(speed, [1,0,1,0,1,0,1,0,1,0,1,0]),
				Row(speed, [0,1,0,1,0,1,0,1,0,1,0,1]),
			],
			12
		)

