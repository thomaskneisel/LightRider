importError = False

try:
	import time
except Exception: 
	print "import time is not available"	
	
try:
	import RPi.GPIO as GPIO
except Exception: 
	print "import RPi.GPIO is not available"	
	importError = True

if importError:
	print "Error!"
	sys.exit()
		
		
class Board(object):
	# Define GPIO pins to use
	# that are connected to 12 LEDs
	CHASER_LIGHTS = [7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22]
	
	# 3 onboard LEDs
	ON_BOARD = [23, 24, 26]
	
	# all together
	ALL_LIGHTS = CHASER_LIGHTS + ON_BOARD

	#inputs
	BUTTONS = [3, 5]
	
	def __init__(self, GPIO, leds=[], buttons=[], verbose=False):
		self._GPIO = GPIO
		self._leds = leds
		self._buttons = buttons
		self.__verbose = verbose

		# Use physical pin numbers references
		self._GPIO.setmode(self._GPIO.BOARD)
		
		self._initLeds()
		self._initButtons()
		
	def __del__(self):
		self._GPIO.cleanup()
		
	def _setupPins(self, pins, mode):
		for pin in pins:
			result = self._GPIO.setup(pin, mode)
			if self.__verbose:
				print "Pin {} set to {}".format(pin, self._getReadableMode(mode))
				
	def _getReadableMode(self, mode):
		return {
			0 : "GPIO.OUT",
			1 : "GPIO.IN",
		}.get(mode, "GPIO.UNKNOWN")
			
	def _initLeds(self):
		self._setupPins(self._leds, self._GPIO.OUT)
	
	def _initButtons(self):
		self._setupPins(self._buttons, self._GPIO.IN)
	
	def addEventCallback(self, button, callback):
			self._GPIO.add_event_detect(button, self._GPIO.RISING)
			self._GPIO.add_event_callback(button, callback, bouncetime=200)
		
	def pressedOne(self):
		print 'pressedOne'
		
	def pressedTwo(self):
		print 'pressedTwo'
		
	def status(self, pins=[]):
		if pins == []:
			pins = self._leds + self._buttons
			
		statusMsg = "\n----------------------------------------\n"
		statusMsg += " Status pins \n"
		statusMsg += "----------------------------------------\n"
			
		for pin in pins:
			statusMsg += "Pin: \t {} \tMode:  \t {} \tValue {} \n".format(pin, self._GPIO.gpio_function(pin), self._GPIO.input(pin))
			
		return statusMsg

	def on(self, led):
		if led in self._leds:
			self._GPIO.output(led, self._GPIO.HIGH)
			if self.__verbose:
				print "LED {} ON".format(led)
			
	def off(self, led):
		if led in self._leds:
			self._GPIO.output(led, self._GPIO.LOW)
			if self.__verbose:
				print "LED {} OFF".format(led)
		
