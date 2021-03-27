import random

class Rando_Bot:
	def __init__(self, size):
		self.board_size = size

	def get_action(self):
		return (random.rand_int(self.size), random.rand_int(self.size))