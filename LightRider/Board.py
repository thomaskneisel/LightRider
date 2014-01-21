try:
	import sys, time
	import RPi.GPIO as GPIO
except Exception, e: 
	print e
	sys.exit(2)

class Board(object):
	# Define GPIO pins to use
	# that are connected to 12 LEDs
	CHASER_LIGHTS = [7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22]
	
	# 3 onboard LEDs
	#  2 bufferd 23, 26
	#  1 unbufferd 26
	ON_BOARD = [23, 24, 26]
	
	# all together
	ALL_LIGHTS = CHASER_LIGHTS + ON_BOARD

	# 2 Buttons
	BUTTONS = [3, 5]
	
	# button callbback bouncetimer
	BOUNCETIME = 300
	
	def __init__(self, GPIO, leds=[], buttons=[], verbose=False, reset=False):
		self._GPIO = GPIO		
		self._leds =  self.ALL_LIGHTS if leds == [] else leds
		self._buttons = self.BUTTONS if buttons == [] else buttons
		self._reset = reset
		self.__verbose = verbose

		# disable warning if we don't reset at the end
		self._GPIO.setwarnings(self._reset)

		# Use physical pin numbers references
		self._GPIO.setmode(self._GPIO.BOARD)
	
		if self.__verbose:	
			self.POST()
		else:
			self._initLeds()
			self._initButtons()

	def POST(self):
		try:
			self._initLeds()
			self._initButtons()

			# Test LEDs
			for led in self._leds:
				self.on(led)
				time.sleep(0.5)
				self.off(led)

			#Test buttons
			for button in self._buttons:
				print "Press button {}".format(button)
				self._GPIO.wait_for_edge(button, GPIO.RISING)
				print "Button {} pressed!".format(button)
		except Exception,e :
			print "Error:", e
			sys.exit(2)
	
	def __del__(self):
		if (self._reset):
			self._GPIO.cleanup()
		
	def _setupPins(self, pins, mode):
		for pin in pins:
			result = self._GPIO.setup(pin, mode, initial=self._GPIO.LOW)
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
		self._GPIO.add_event_callback(button, callback, bouncetime=self.BOUNCETIME)

	def removeEventDetect(self, button):
		self._GPIO.remove_event_detect(button)
		
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
		
