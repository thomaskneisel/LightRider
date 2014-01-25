from Sequence import Sequence 
from Row import Row

class Kitt(Sequence):
	def __init__(self, speed=0.08):
		Sequence.__init__(
			self, [
				Row(speed, [0,0,0,0,0,1,1,0,0,0,0,0]),
				Row(speed, [0,0,0,0,1,0,0,1,0,0,0,0]),
				Row(speed, [0,0,0,1,0,0,0,0,1,0,0,0]),
				Row(speed, [0,0,1,0,0,0,0,0,0,1,0,0]),
				Row(speed, [0,1,0,0,0,0,0,0,0,0,1,0]),
				Row(speed, [1,0,0,0,0,0,0,0,0,0,0,1]),
				Row(speed, [0,1,0,0,0,0,0,0,0,0,1,0]),
				Row(speed, [0,0,1,0,0,0,0,0,0,1,0,0]),
				Row(speed, [0,0,0,1,0,0,0,0,1,0,0,0]),
				Row(speed, [0,0,0,0,1,0,0,1,0,0,0,0]),
				Row(speed, [0,0,0,0,0,1,1,0,0,0,0,0]),
			]
		)

