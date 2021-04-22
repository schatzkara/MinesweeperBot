import math
from Constants import *

'''A class representing a tile on the board.
'''
class Tile:
	'''Constructor for Tile objects.
	Initializes each tile to be unclicked and have the given position and number.
	If the number is the designated MINE_VAL, then the tile is a mine, otherwise it is not.
	:param position: (tuple) the board position
	:param number: (int) the number in the tile
	'''
	def __init__(self, position, number):
		self.clicked = False
		self.number = number
		self.position = position
		self.isMine = False
		if self.number == MINE_VAL:
			self.isMine = True

