import random

class KBA:
	def __init__(self, size):
		self.board_size = size
		self.knowledge_base = []

	def get_action(self):
		return (random.rand_int(self.size), random.rand_int(self.size))

	def tell(self, row, col, number):
		self.knowledge_base.add("Number({},{})={}".format(row, col, number))
