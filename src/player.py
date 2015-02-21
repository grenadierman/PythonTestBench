# Models generic player statistics REVIEW PYTHONIC SETTERS/GETTERS
from constants import *

class Player:

	def __init__(self, character):
		# Initialize player data
                self.character = character
                self.stats = [0, 0, 0, 0, 0, 0, 0, 0]
                self.location = 'Unknown'

		if character == 'test_guy_1':
			self.stats[STAMINA] = 5
			self.stats[SANITY] = 5
			self.stats[STRENGTH] = 3
			self.stats[INTELLECT] = 5
			self.stats[BRAVERY] = 4
			self.stats[SPEED] = 3
			self.stats[AGILITY] = 2
			self.stats[LUCK] = 3
			self.stats[FOCUS] = 2
			self.stats[CURSE] = 0 #I AM LACHDANAN AND I AM CURSED AT 1 BLESSED AT -1
			self.location = 'loc1'

		elif character == 'test_guy_2':
			self.stats[STAMINA] = 10
			self.stats[SANITY] = 2
			self.stats[STRENGTH] = 6
			self.stats[INTELLECT] = 2
			self.stats[BRAVERY] = 5
			self.stats[SPEED] = 4
			self.stats[AGILITY] = 1
			self.stats[LUCK] = 2
			self.stats[FOCUS] = 2
			self.stats[CURSE] = 0 #I AM LACHDANAN AND I AM CURSED AT 1 BLESSED AT -1
			self.location = 'loc5'

