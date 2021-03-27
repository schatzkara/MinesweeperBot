BOARD_SIZE = 4
MINE_VAL = float('inf')

MINE_LOCATIONS = [(0, 0), (1, 2), (2, 1)]
NUM_MINES = len(MINE_LOCATIONS)


WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
TITLE_FONT = ("Arial", 30)
TILE_FONT = ("Arial", 40)
BOARD_COLOR = '#776e65'

TILE_WIDTH = 4
TILE_HEIGHT = 2
TILE_PADX = 5
TILE_PADY = 5

text_color_dict = {0: '#BDAD9E',
                   2: '#BDAD9E',
                   4: '#ede0c8',
                   8: '#f9f6f2',
                   16: '#f9f6f2',
                   32: '#f9f6f2',
                   64: '#f9f6f2',
                   128: '#f9f6f2',
                   256: '#f9f6f2',
                   512: '#f9f6f2',
                   1024: '#f9f6f2',
                   2048: '#f9f6f2'
                   }

tile_color_dict = {0: '#BDAD9E',
                   2: '#eee4da',
                   4: '#ede0c8',
                   8: '#f2b179',
                   16: '#f59563',
                   32: '#f67c5f',
                   64: '#f65e3b',
                   128: '#edcf72',
                   256: '#edcc61',
                   512: '#edc850',
                   1024: '#edc53f',
                   2048: '#edc22e'
                   }