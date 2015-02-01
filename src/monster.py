# Encapsulates generic monster information

class Monster:
	
	_mname = 'SPOOKY NAME'
	_monster = 'GENERIC SPOOKY'
	_mstats = [0, 0, 0, 0, 0, 0]
	
	def __init__(self, mname):
		# Set monster stats
		self._mname = mname
		#raise NotImplementedError
