#!/usr/bin/env python
#
# octoprint event interface
#

import argparse
from OctoPrint import *

def main():
        parser = argparse.ArgumentParser(prog="octoprint event interface")
        parser.add_argument("--debug", action="store_true", dest="debug",
                help="Enable debug mode")

	parser.add_argument("-e", "--event", action="store", type=str, dest="event",
		help="OctoPrint event name", required=True, nargs=1, choices=["Startup", 
			"Connected", "Disconnected", "ClientOpen", "ClientClosed", "PowerOn",
			"PowerOff", "Upload", "FileSelected", "TransferStart", "TransferDone",
			"PrintStarted", "PrintFailed", "PrintDone", "PrintCancelled", "Home",
			"ZChange", "Paused", "Waiting", "Cooling", "Alert", "Conveyor", "Eject",
			"CaptureStart", "CaptureDone", "MovieDone", "EStop", "Error"])

	parser.add_argument("-d", "--data", action="store", type=str, dest="data",
		help="the data associated with the event (not all events have data, when they do, it's often a filename)")

	parser.add_argument("-f", "--filename", action="store", type=str, dest="filename",
                help="filename of the current print (not always the same as data filename), 'NO FILE' if not available")

	parser.add_argument("-p", "--progress", action="store", type=float, dest="progress",
                help="the progress of the print in percent, 0 if not available")

	parser.add_argument("-z", "--currentZ", action="store", type=int, dest="currentZ",
                help="the current Z position of the head if known, -1 if not available")

	parser.add_argument("-t", "--now", action="store", type=str, dest="now",
                help="the date and time of the event in ISO 8601")

	parser.add_argument("--payload", action="store", type=str, dest="payload", 
		help="the event payload read https://github.com/foosel/OctoPrint/wiki/Available-Events\#events")

	# may be in the future
#        parser.add_argument("-c", "--config", action="store", dest="config",
#                help="Specify the config file to use. OctoPrint needs to have write access for the settings dialog to work. Defaults to ~/.octoprint/config.yaml")

	# debug issues
#	parser.add_argument("-con", "--connected", action="store_true", dest="connected",
#                help="Printer connected action")

        args = parser.parse_args()

	print
	print args
	print

	octoprint = OctoPrint()
	octoprint.event(args)


# lets rock
if __name__ == "__main__":
        main()
