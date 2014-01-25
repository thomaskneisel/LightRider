from Sequence import Sequence 
from Row import Row

class AllOn(Sequence):
	def __init__(self, speed=1):
		Sequence.__init__(
			self, [
				Row(speed, [1,1,1,1,1,1,1,1,1,1,1,1]),
			],
			9999
		)

