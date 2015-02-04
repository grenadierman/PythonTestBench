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
for loc in context.world.locations:
    print 'Location: %s Players: %s' % (loc, context.world.locations[loc][PLAYERS])

print '\n####### Players #######'
print 'Context contains players %s' % context.players.keys()



print '\nEnd of test\n'
crap = raw_input()
