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
		board_size = self.get_int('What number of rows and columns would you like? ')
		num_mines = self.get_int('How many mines would you like out of the {} tiles? '.format(board_size**2))
		self.bot = self.get_bot_type(board_size)

		self.board = Board(board_size, num_mines)
		# self.bot = Rando_Bot(BOARD_SIZE)
		# self.bot = KBA(board_size)
		self.gui = Graphics(self.board, self.bot)
		self.gui.mainloop()

	'''Gets an integer input.
	:param prompt: (str) the prompt for the input
	:return: (int) the user input
	'''
	def get_int(self, prompt):
		correct = False
		while not correct:
			try:
				result = int(input(prompt))
				correct = True
			except:
				print('Sorry, try again.')

		return result

	'''Gets the input for the bot type.
	:param board_size: (int) the size of the board
	:return: the appropriate Bot object
	'''
	def get_bot_type(self, board_size):
		correct = False
		while not correct:
			mode = (input('Would you like to use the knowledge-based agent or the random bot? (type "random" or "kba") '))
			if mode == 'random':
				bot = Rando_Bot(board_size)
				correct = True
			elif mode == 'kba':
				bot = KBA(board_size)
				correct = True
			else:
				print('Sorry, try again.')

		return bot


if __name__ == "__main__":
	Driver()
