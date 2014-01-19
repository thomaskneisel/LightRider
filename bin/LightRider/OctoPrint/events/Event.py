from LightRider.Sequence import Sequence

class Event(object):
	def __init__(self):
		print "Event __init__"
		print __name__
		print
		speed = 0.2	
		self.sequence = Sequence(speed, [[1,1,0,0,0,1,1,1,0,0,1,1,0],[0,1,1,1,0,0,0,1,1,0,0,1]])		
		self.leds = [
			[23, 1],
			[24, 0],
			[26, 1]
		]
