from constants import *
class Location:

    def __init__(self, name, north='', south='', east='', west=''):
	self.name = name
        self.north = north 
        self.south = south
        self.east = east
        self.west = west
        self.players = {}

    def add_player(self, name):
        self.players[name] = name

    def get_players(self):
        return self.players.keys()

    def get_connections(self):
        return (self.north, self.south, self.east, self.west)

# REDO MAP CLASS, SOMETHING IS FUCKY WITH CLASS/INSTANCE VARIABLES
class Worldmap:

    # Build world map
    def __init__(self):

        self.locations = {}

        try:
       	    world_dat = open('world.dat')

       	except:
       	    # switch to proper logging later
       	    print 'MISSING WORLD DATA - FATAL ERROR'

       	numloc = int(world_dat.readline().split()[0])

       	for loc in xrange(numloc):
            locname = world_dat.readline().split()
            conn = world_dat.readline().split()

            north = ''
            south = ''
            east = ''
            west = ''

            for x in xrange(len(conn)/2):
                if conn[2*x] == 'n':
                    north = conn[2*x+1]  
                elif conn[2*x] == 's':
                    south = conn[2*x+1]
                elif conn[2*x] == 'e':
                    east = conn[2*x+1]
                elif conn[2*x] == 'w':
                    west = conn[2*x+1]
            
                self.locations[locname[0]] = Location(locname[0], north, south, east, west)

    # Travers world map using Dijkstras algorithm
    def shortest_paths(self):
            pass

    # Might not have to use
    def set_location(self, player, newloc, curloc='noloc'):
        if curloc == 'noloc':
            self.locations[newloc].add_player(player.get_name())
        else:
            self.locations[newloc].add_player(player.get_name())
            #del self.locations[curloc]._players[player.get_name()] 

    def get_loc_players(self, loc):
        return self.locations[loc].get_players()

    def get_locations(self):
        return self.locations.keys()

    def get_connections(self, loc):
        return self.locations[loc].get_connections()

