import time

class LightRider(object):

	def __init__(self, board, verbose=False):
		self._board = board
		self._sequences = []
		self.__verbose = verbose

	def addSequence(self, sequence):
		self._sequences.append(sequence)

	def getSequence(self, index):
		return self._sequences[index]

	def run(self, sequence):
		data = sequence.getSequence()
		self._speed = sequence.speed
		for row in data:
	 		map(self._led, self._board.CHASER_LIGHTS, row)
			
	def _led(self, pin, value):
		if pin == None:
                        return False
		if self.__verbose:	
			print "Pin {} to {}".format(pin, value),
		if value == 1:
			self._board.on(pin)
			print "self._board.on({})".format(pin)
		else:
			self._board.off(pin)
			print "self._board.off({})".format(pin)

		time.sleep(0.15)


