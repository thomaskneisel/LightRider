import time

class LightRider(object):

	def __init__(self, board, verbose=False):
		self._board = board
		self._sequences = []
		self._speed = 0.0001
		self.__verbose = verbose

	def addSequence(self, sequence):
		self._sequences.append(sequence)

	def getSequence(self, index):
		return self._sequences[index]

	def run(self, sequence):
		data = sequence.getSequence()
		for row in data:
	 		map(self.led, self._board.CHASER_LIGHTS, row)
			time.sleep(sequence.speed)
			
	def led(self, pin, value=1, speed=0.0001):
		if speed <= 0:
			speed = self._speed
		if pin == None:
                        return False
		if self.__verbose:
			print "[{}]Pin {} to {}".format(__name__, pin, value),

		if value == 1:
			self._board.on(pin)
		else:
			self._board.off(pin)

		time.sleep(speed)


