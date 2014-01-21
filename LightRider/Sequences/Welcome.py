
from Sequence import Sequence
from Row import Row
from Kitt import Kitt

class Welcome(Sequence):
	def __init__(self):		
		kitt = Kitt()
		Sequence.__init__(self, kitt.getRows())

