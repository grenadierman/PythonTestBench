import pygame

import logging

from player import Player
from context import Context

from constants import *

"""

Plan on changing game loop to a dedicated class to clean up look and properly
handle state. This will do for now

"""
def move_dot(dot, x, y, wnd):

	if dot == 'red':
		pygame.draw.circle(wnd, RED, (x, y), 45, 0)
	elif dot == 'blue':
		pygame.draw.circle(wnd, BLUE, (x, y), 45, 0)


def main():
	"""		
	numplayers = 0
	playerchars = []
	"""

	# Setup logging better later
	if DEBUG:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.ERROR)

	log = logging.getLogger(' ' + __name__)

	pygame.init()
	window = pygame.display.set_mode(WINDOW_SIZE)

	"""
	# DEBUG initialization context - move to seperate file later
	if DEBUG:
		numplayers = 2 
		playerchars.append(('DiGiTALQU33F', 'test_guy_1'))
		playerchars.append(('iRONVAGiNA', 'test_guy_2'))
		log.debug(' Starting up in debug mode')

	game_context = Context(numplayers, playerchars)
	"""

	state = 'startup'

	# Main game loop
	while 1: 
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				exit()
			if ev.type == pygame.KEYDOWN:
				if (ev.key == pygame.K_q):
					exit()
		if state == 'startup':

			window.fill(GREY)

			x1 = (WINDOW_SIZE[0]/2) - 150 
			x2 = (WINDOW_SIZE[0]/2) + 50 
			y1 = (WINDOW_SIZE[1]/8)
			y2 = (WINDOW_SIZE[1]/8) + 150
			y3 = (WINDOW_SIZE[1]/8) + 300 

			pygame.draw.rect(window, WHITE, (x1, y1, 100, 100), 0)
			pygame.draw.rect(window, WHITE, (x2, y1, 100, 100), 0)
			pygame.draw.rect(window, WHITE, (x1, y2, 100, 100), 0)
			pygame.draw.rect(window, WHITE, (x2, y2, 100, 100), 0)
			pygame.draw.rect(window, WHITE, (x1, y3, 100, 100), 0)
			pygame.draw.rect(window, WHITE, (x2, y3, 100, 100), 0)
			move_dot('red', x1+50, y1+50, window)
			move_dot('blue', x2+50, y3+50, window)

			pygame.display.update()
			state = 'generic'

		elif state == 'generic':
			pass

		pygame.display.flip()

	raise Exception('Main loop dun goofed') # Shouldn't reach this

if __name__ == '__main__':

	main()
