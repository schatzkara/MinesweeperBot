import random
from tile import Tile


class Board:
    """
    Constructor for Board objects.
    Board objects have the following fields:
        size: the number of tiles in each row and column of the board
        start_tiles: the number of tiles that the board starts with
        grid: a 2D array representing the board
    """
    def __init__(self, size, start_tiles):
        self.size = size
        self.start_tiles = start_tiles
        self.grid = [[None for x in range(self.size)] for y in range(self.size)]
        """ randomly put 2 tiles (either 2 or 4) on the board """
        # self.init_grid()
        # self.display()

    """
    Accessor method for the grid
    @return the field grid
    """
    def get_grid(self):
        return self.grid