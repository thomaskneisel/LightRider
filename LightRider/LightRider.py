import time, sys

class LightRider(object):
	BUTTON_ONE = 3
	BUTTON_TWO = 5

	def __init__(self, board, verbose=False):
		self._board = board
		self._speed = 0.0001
		self.__verbose = verbose
		self._sequence = None
		self._break = False
		self._pressed = 0

	def run(self, sequence):
		self._sequence = sequence
		self._break = False

		#activate Button callback         
		self._board.addEventCallback(self.BUTTON_ONE, self._breakSequence)
                self._board.addEventCallback(self.BUTTON_TWO, self._breakSequence)

		n = 0
		while n < sequence.repeat or -1 == sequence.repeat:			
			for row in sequence.getRows():
				if self._break: break
				map(self.led, self._board.CHASER_LIGHTS, row.values)
				time.sleep(row.speed)
			n +=1

		self._board.removeEventDetect(self.BUTTON_ONE)
		self._board.removeEventDetect(self.BUTTON_TWO)	
	
	def _breakSequence(self, pin):
		if 0 != self._pressed and pin != self._pressed:
			print "Both Buttons pressed, exit."
			sys.exit(2)

		self._pressed = pin
		if None == self._sequence:
			self._pressed = 0
			return None

		self._sequence.repeat = 0		
		if pin == self.BUTTON_TWO:
			self._break = True

		self._pressed = 0
		
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


