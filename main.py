#!/usr/bin/env python
import sys
import getopt
import argparse

class Controller(object):

	def __init__():
		pass

	def 


# sys.argv[0] = filname
#for value in sys.argv:
#	print value
# array[x:] = x to end of list
#main(sys.argv[1:])

try:                                
	opts, args = getopt.getopt(sys.argv, "hg:d", ["help", "grammar="])
except getopt.GetoptError:           
	usage()
	sys.exit(2)

for name in opts:
	print name

for name in args:
	print name

def usage():
	print "Help"
	print "bla bla"
	pass



parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)
