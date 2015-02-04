import pygame

from player import Player
from context import Context
from constants import *

numplayers = 2
testplayers = []

testplayers.append(('DiGiTALQU33F', 'test_guy_1'))
testplayers.append(('iRONVAGiNA', 'test_guy_2'))

context = Context(numplayers, testplayers)

print '\n###### Locations ######'
for loc in context.world.get_locations():
    print 'Location: %s Players: %s' % (loc, context.world.get_loc_players(loc))
    con = context.world.get_connections(loc)
    print 'Location connections:\nNorth: %s\nSouth: %s\nEast: %s\nWest: %s' % (con[0], con[1], con[2], con[3])

print '\n####### Players #######'
print 'Context contains players %s' % context.players.keys()



print '\nEnd of test\n'
crap = raw_input()
