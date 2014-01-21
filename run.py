#!/usr/bin/env python
#
# LightRider command line runner
# 

from LightRider import Board, LightRider, Sequences
from LightRider.Sequences.Sequence import factory
import sys, argparse
import RPi.GPIO as GPIO

def main():
	parser = argparse.ArgumentParser(prog="LightRider CLI")

	parser.add_argument("--debug", action="store_true", dest="debug",
        	help="Enable debug mode")

	parser.add_argument("-r", "--reset", action="store_true", dest="reset",
                help="Reset GPIO at end", default=True)

	parser.add_argument("-p", "--POST", action="store_true", dest="post",
		help="include Board Power On 'Self' Test")

	parser.add_argument("-s", "--sequence", action="store", type=str, dest="sequence",
		help="running Sequence")

	parser.add_argument("-st", "--status", action="store_true", dest="status",
		help="show Board status at startup")

	parser.add_argument("-l", "--leds", action="store", dest="leds", type=int,
		help="GPIO pins (Hardware pins!) to use as LEDs", nargs="*")

	parser.add_argument("-b", "--buttons", action="store", dest="buttons", nargs="*", type=int,
		help="GPIO pins (Hardware pins!) to use as Buttons (recommend pins 3 and 5)")

	args = parser.parse_args()
	
	leds = args.leds if args.leds else Board.ALL_LIGHTS
	buttons = args.buttons if args.buttons else Board.BUTTONS

	## Board
	board = Board(GPIO, leds, buttons, args.debug, args.reset)

	## POST
	if args.post:
		board.POST()

	## Status
	if args.status:
		print board.status()

	lr = LightRider(board, args.debug)
	## Sequence
	if args.sequence:		
		try:
			lr = LightRider(board, args.debug)
			sequence = factory(args.sequence)
			lr.run(sequence)
		except Exception, e: 		
			print
			print "Error :", e
			sys.exit(2)


# lets rock
if __name__ == "__main__":
        main()
