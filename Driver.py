from Board import Board
from Graphics import Graphics
from Rando_Bot import Rando_Bot
from KBA import KBA
import keyboard
import random
from Constants import *


'''Serves as the driver for running the Minesweeper bot.
'''
class Driver:
	'''Initializes the trial of the bot.
	Gets the desired board size as well as the desired number of mines and runs the KBA accordingly. 
	'''
	def __init__(self):
		board_size = int(input('What number of rows and columns would you like? '))
		num_mines = int(input('How many mines would you like out of the {} tiles? '.format(board_size**2)))
		mode = int(input('Would you like to use the knowledge-based agent or the random bot? (type "random" or "kba")'))
		if mode == 'random':
			self.bot = Rando_Bot(board_size)
		elif mode == 'kba':
			self.bot = KBA(board_size)
		self.board = Board(board_size, num_mines)
		# self.bot = Rando_Bot(BOARD_SIZE)
		# self.bot = KBA(board_size)
		self.gui = Graphics(self.board, self.bot)
		self.gui.mainloop()


if __name__ == "__main__":
	Driver()
