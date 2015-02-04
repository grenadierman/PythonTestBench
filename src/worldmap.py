from constants import *

class Worldmap:

    # Build world map
    def __init__(self):

        self.locations = {}

        try:
       	    world_dat = open('../bin/world.dat')

       	except:
       	    # Switch to proper logging later
       	    print 'MISSING WORLD DATA - FATAL ERROR'

       	numlocations = int(world_dat.readline().split()[0])

       	for lines in xrange(numlocations):
            locname = world_dat.readline().split()[0]
            self.locations[locname] = ['', '', '', '', []]

            conn = world_dat.readline().split()

            for x in xrange(len(conn)/2):
                if conn[2*x] == 'n':
                    self.locations[locname][NORTH] = conn[2*x+1]  
                elif conn[2*x] == 's':
                    self.locations[locname][SOUTH] = conn[2*x+1]
                elif conn[2*x] == 'e':
                    self.locations[locname][EAST] = conn[2*x+1]
                elif conn[2*x] == 'w':
                    self.locations[locname][WEST] = conn[2*x+1]

    # Travers world map using Dijkstras algorithm
    def shortest_paths(self):
            pass
