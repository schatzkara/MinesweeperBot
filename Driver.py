from Board import Board
from Graphics import Graphics
from Rando_Bot import Rando_Bot
from KBA import KBA
import keyboard
import random
from gui_constants import *
import time

class Driver:
    def __init__(self):
        board_size = int(input('What number of rows and columns would you like? '))
        num_mines = int(input('How many mines would you like out of the {} tiles? '.format(board_size**2)))
        self.board = Board(board_size, num_mines)
        # self.bot = Rando_Bot(BOARD_SIZE)
        self.bot = KBA(board_size)
        start = time.time()
        self.gui = Graphics(self.board, self.bot)
        self.gui.mainloop()
        end = time.time()

        print(end - start)


if __name__ == "__main__":
    Driver()
