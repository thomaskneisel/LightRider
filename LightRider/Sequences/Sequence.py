import time,sys,inspect
from Row import Row

## factory in namespace ?!...
def factory(name, args=[]):
	
	try:
                classAttr = getattr(__import__(__name__).Sequences, name)
		print "Create {} Sequence".format(name)
		sequence = apply(classAttr, args)
	except Exception, e:
		print
		print "Error:",e
		sequence = Sequence([Row(2,[1]), Row(1,[0])])
	
	return sequence

class Sequence(object):
	def __init__(self, rows=[], repeat=1):
		self.rows = rows
		self.repeat = repeat
			
	def appendRows(self, rows):
		self.rows + rows
		
	def appendRow(self, row):
		self.rows.append(row)

	def getRows(self):
		return self.rows
		
	def showRows(self):
		print "Sequence"
		map(self._showRow, self.rows)
		
	def _showRow(self, row):		
		for value in row.values:
			if 0 == value:
				print " ",
			else:
				print "*",
				time.sleep(row.speed)
			print

