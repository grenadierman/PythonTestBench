"""

Contains generic data for game context. 

To do: Monster / Map / Old One / Curse data

Notes:
	Should players be stored as name/object pair? 

"""
from player import Player
from constants import *

import logging
from random import randint

class Context:
	
	# Setup context logging
	if DEBUG:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.ERROR)

	_log = logging.getLogger(' ' + __name__)


	# Players
	_numplayers = -1 
	_players = {} 

	"""	
	# Old one stats
	_oldone = 'SUPER DUPER SPOOKY'

	# World stats -  placeholder for now
	_curse = 'SPOOKY CURSE'
	"""
	
	def __init__(self, numplayers, playerchars):

		self._numplayers = int(numplayers)

		for x in xrange(self._numplayers):
			self._players[playerchars[x][0]] = Player(playerchars[x][0], playerchars[x][1])

		if DEBUG:
			for key in self._players:
				self._log.debug(' %s, %s', self._players[key]._name, self._players[key]._character)

	# Might not be needed
	def set_old_one(self, placeholder):
		pass

	# Player moving logic
	def move_player(self, placeholder):
		pass

	# Monster moving logic
	def move_monster(self, placeholder):
		pass

	# Might move this function to another file once more utils surface
	def roll(self):
		return randint(1, 6)


