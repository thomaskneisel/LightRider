import inspect
import Sequences 

class SequenceInspector(object):
	EXCLUDES = ['Row','Sequence']

	def __init__(self):
		self._sequences = {}
		self._fetchSequences()
		
	def _fetchSequences(self):
		for name, value in inspect.getmembers(Sequences):
			if name in self.EXCLUDES:
				continue

			if inspect.isclass(value):
				self._sequences[name] = value()			
                        
	def getSequences(self):
		return self._sequences.items()
