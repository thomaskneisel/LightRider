import time

class LightRider(object):
	BUTTON_ONE = 3
	BUTTON_TWO = 5

	def __init__(self, board, verbose=False):
		self._board = board
		self._speed = 0.0001
		self.__verbose = verbose
		self._sequence = None
		self._break = False

	def run(self, sequence):
		self._sequence = sequence
		self._break = False
		#activate Button callback         
		self._board.addEventCallback(self.BUTTON_ONE, self._breakSequence)

		n = 0
		while n < sequence.repeat or True == sequence.repeat:
			for row in sequence.getRows():
				if self._break: break
				map(self.led, self._board.CHASER_LIGHTS, row.values)
				time.sleep(row.speed)
			n +=1
	
	def _breakSequence(self, pin):
		if None == self._sequence or 0 == self._sequence.repeat:
			return None
		self._sequence.repeat = 0
		self._sequence = None
		self._board.removeEventDetect(pin)
		self._break = True
		
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


