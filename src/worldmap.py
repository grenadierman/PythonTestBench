class Location:
	_name = 'Unknown'
	_north = None
	_south = None
	_east = None
	_west = None
	_players = []

	def __init__(self, name):
		self._name = name

class Map:

	_locations = []

	# Build world map
	def __init__(self):

		try:
			world_dat = open('world.dat')

		except:
			# switch to proper logging later
			print 'MISSING WORLD DATA - FATAL ERROR'

		numloc = int(world_dat.readline().split()[0])

		for loc in xrange(numloc):
			locname = world_dat.readline().split()
			_locations.append(Location(locname[0]))
			conn = world_dat.readline().split()

			for x in xrange(len(conn)/2):
				if conn[2*x] == 'n':
					pass
				elif conn[2*x] == 's':
					pass
				elif conn[2*x] == 'e':
					pass
				elif conn[2*x] == 'w':
					pass

	
	# Travers world map using Dijkstras algorithm
	def shortest_paths(self):
		pass

	# Might not have to use
	def set_location(self):
		pass


