#
#
# octoprint event interface
#
#
import sys, os, argparse
import RPi.GPIO as GPIO

# import LightRider Project files
# append project path relative to script path if calls via subfolder eg "bin/LightRider/octoprint"
sys.path.append(os.path.abspath(__file__ + '/../../../..'))
from LightRider import *

# import event sequences
import events

class OctoPrint(object):
	def __init__(self, debug=True):
		self._debug = debug		
		self._lightRider = LightRider(self._getBoard(), self._debug)

	def _getBoard(self):
		return Board(GPIO, Board.ALL_LIGHTS, Board.BUTTONS, self._debug)

	def event(self, event):
		event.name = event.event[0]
		eventSequence =  self.eventFactory(event)

		if self._debug:
			print "\n[{}]Event: \n {} \n".format(__name__, event)
			print "\n[{}]EventSequence: \n {} \n {} \n".format(__name__, eventSequence, eventSequence.sequence)

		# sequence handling
		if eventSequence.sequence:
	                if self._debug:
                		print "\n[{}]EventSequence: \n {} \n {} \n".format(__name__, eventSequence, eventSequence.sequence)
			self._lightRider.run(eventSequence.sequence)

		# single led handling
		if eventSequence.leds:
	                if self._debug:
	                        print "\n[{}]Leds: \n {} \n".format(__name__, eventSequence.leds)
			for led in eventSequence.leds:
				pin = led[0]
				value = led[1]
				self._lightRider.led(pin, value)		
			
	def eventFactory(self, event, args=[]):
		try:
			classAttr = getattr(events, event.name)
			eventObject = apply(classAttr, args)
		except Exception, e:
			if self._debug:
				print e
			eventObject = events.Event()

                return eventObject

