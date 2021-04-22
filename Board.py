import random
from Tile import Tile
from Constants import *


'''A class representing the Minesweeper game board
'''
class Board:
	'''Constructor for Board objects.
	Initializes the grid according to the given size and number of mines.
	:param size: (int) the board size
	:param num_mines: (int) the number of mines that should be placed on the board
	'''
	def __init__(self, size, num_mines):
		self.size = size
		self.num_mines = num_mines
		self.grid = [[None for x in range(self.size)] for y in range(self.size)]
		self.init_grid(self.pick_mine_locations(self.size, self.num_mines))
		# self.display()

	'''Randomly picks the appropriate number of locations for mines on the board.
	:param size: (int) the board size
	:param num_mines: (int) the number of mines that should be placed on the board
	:return: (list) the list of mine locations
	'''
	def pick_mine_locations(self, board_size, num_mines):
		mine_locs = []
		for x in range(num_mines):
			found = False
			while not found:
				i, j = random.randint(0, board_size-1), random.randint(0, board_size-1)
				if (i, j) not in mine_locs:
					found = True
			mine_locs.append((i, j))

		return mine_locs

	'''Initializes the grid with a mine in each of the given mine locations and the appropriate number in each other tile.
	:param mine_locations: (list) the list of mine locations
	'''
	def init_grid(self, mine_locations):
		# first place all the mines appropriately
		for row, col in mine_locations:
			self.grid[row][col] = Tile(position=(row, col), number=MINE_VAL)

		# for any tile which was not initialized to be a mine, determine the appropriate number to initialize it with
		for row in range(len(self.grid)):
			for col in range(len(self.grid[row])):
				if self.grid[row][col] is None:
					self.grid[row][col] = Tile(position=(row, col), number=len(self.adjacent_mines(row, col)))

	'''Displays the board to the console in a readable format.
	:param clicked: (boolean) True if only the clicked tiles should be shown, False otherwise
	'''
	def display(self, clicked=True):
		for row in range(len(self.grid)):
			for col in range(len(self.grid[row])):
				if self.grid[row][col] is not None:
					if not clicked or self.grid[row][col].clicked:
						print(self.grid[row][col].number)
					else:
						print(" ")
				else:
					print(" ")
			print("\n")

	'''Gets the list of adjacent mines to the given tile.
	:param row: (int) the row of the given tile
	:param col: (int) the column of the given tile
	:return: (list) the list of the adjacent mines
	'''
	def adjacent_mines(self, row, col):
		mines = []
		adjacent_tiles = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
		for row, col in adjacent_tiles:
			if row >= 0 and row < self.size and col >= 0 and col < self.size:
				if self.grid[row][col] is not None and self.grid[row][col].isMine:
					mines.append((row, col))

		return mines

	'''Clicks the given tile on the board by setting its clicked attribute to true.
	:param row: (int) the row of the given tile
	:param col: (int) the column of the given tile
	'''
	def click_tile(self, row, col):
		if self.grid[row][col] is not None:
			self.grid[row][col].clicked = True

	'''Determines if the board is a dead board, i.e. the game is over.
	:return: (boolean) True if the game is over, False otherwise
	'''
	def dead(self):
		for row in range(len(self.grid)):
			for col in range(len(self.grid[row])):
				if self.grid[row][col] is not None and self.grid[row][col].isMine and self.grid[row][col].clicked:
					return True

		return False

	'''Determines if the board is in a winning state.
	:return: (boolean) True if the board has been won, False otherwise
	'''
	def win(self):
		num_clicked_not_mine = 0
		for row in range(len(self.grid)):
			for col in range(len(self.grid[row])):
				if not self.grid[row][col].isMine and self.grid[row][col].clicked:
					num_clicked_not_mine += 1
				# if self.grid[row][col] is not None:
				#     if self.grid[row][col].isMine and self.grid[row][col].clicked:
				#         return False
				#     if not self.grid[row][col].isMine and not self.grid[row][col].clicked:
				#         return False

		return (num_clicked_not_mine + self.num_mines) == (self.size * self.size)
