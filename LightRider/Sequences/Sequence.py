import time

class Sequence(object):
	def __init__(self, rows=[]):
		self.rows = rows
			
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

