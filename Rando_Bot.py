import random

'''A class representing a Random Agent for the Minesweeper game.
'''
class Rando_Bot:
	'''Constructor for the Rando_Bot.
	'''
	def __init__(self, board_size):
		self.board_size = board_size

	'''Gets a random action, i.e. picks a random unclicked tile to click.
	'''
	def get_action(self, board):
		found = False
		while not found:
			i, j = random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)
			if not board[i][j].clicked:
				found = True

		return i, j

	# placeholder so the same program runs for both bots
	def tell(self, row, col, number):
		return