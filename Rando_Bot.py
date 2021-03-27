import random

class Rando_Bot:
	def __init__(self, size):
		self.size = size

	def get_action(self):
		return (random.randint(0, self.size-1), random.randint(0, self.size-1))