import random
from Tile import Tile
from constants import *


class Board:
    """
    Constructor for Board objects.
    Board objects have the following fields:
        size: the number of tiles in each row and column of the board
        start_tiles: the number of tiles that the board starts with
        grid: a 2D array representing the board
    """
    def __init__(self, size, mine_locations):
        self.size = size
        self.grid = [[None for x in range(self.size)] for y in range(self.size)]
        self.init_grid(mine_locations)
        # self.display()

    def init_grid(self, mine_locations):
        for row, col in mine_locations:
            self.grid[row][col] = Tile(position=(row, col), number=MINE_VAL)

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] is None:
                    self.grid[row][col] = Tile(position=(row, col), number=len(self.adjacent_mines(row, col)))

    def display(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] is not None and self.grid[row][col].clicked:
                    print(self.grid[row][col].number)
                else:
                    print(" ")
            print("\n")

    """
    Accessor method for the grid
    @return the field grid
    """
    def get_grid(self):
        return self.grid

    def adjacent_mines(self, row, col):
        mines = []
        adjacent_tiles = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
        for row, col in adjacent_tiles:
            if row >= 0 and row < self.size and col >= 0 and col < self.size:
                if self.grid[row][col] is not None and self.grid[row][col].isMine:
                    mines.append((row, col))

        return mines

    def click_tile(self, row, col):
        if self.grid[row][col] is not None:
            self.grid[row][col].clicked = True

    def dead(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] is not None and self.grid[row][col].isMine and self.grid[row][col].clicked:
                    return True

        return False


    def win(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] is not None and (not self.grid[row][col].isMine) and (not self.grid[row][col].clicked):
                    return False

        return True
