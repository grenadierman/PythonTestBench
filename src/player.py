# Models generic player statistics REVIEW PYTHONIC SETTERS/GETTERS
from constants import *

class Player:

	_name = 'Guest'
	_character = 'Stranger'
	_stats = [0, 0, 0, 0, 0, 0, 0, 0]
	_pos = -1

	def __init__(self, name, character):
		# Initialize player data
		self._name = name

		if character == 'test_guy_1':
			self._character = character	
			self._stats[HEALTH] = 5
			self._stats[SANITY] = 5
			self._stats[STRENGTH] = 3
			self._stats[INTELLECT] = 5
			self._stats[BRAVERY] = 4
			self._stats[SPEED] = 3
			self._stats[AGILITY] = 2
			self._stats[LUCK] = 3
			self._pos = 0

		elif character == 'test_guy_2':
			self._character = character	
			self._stats[HEALTH] = 10
			self._stats[SANITY] = 2
			self._stats[STRENGTH] = 6
			self._stats[INTELLECT] = 2
			self._stats[BRAVERY] = 5
			self._stats[SPEED] = 4
			self._stats[AGILITY] = 1
			self._stats[LUCK] = 2
			self._pos = 4

	def get_pos(self):
		return self._pos




