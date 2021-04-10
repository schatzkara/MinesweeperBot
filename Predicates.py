
class Predicates(Enum):
    CLICKED = 0
    ONE = 1
    TWO = 2
    THREE = 3
    SAT = 4
    MINE = 5
    DIFF = 6
    ADJ = 7
    ADJ_MINE = 8
    ADJ_CLICKED = 9
    NUM_ADJ = 10
    NUM_ADJ_MINES = 11
    NUM_ADJ_CLICKED = 12

class Clicked:
    def __init__(self, tile):
        self.tile = tile

    def __eq__(self, other):
        return isinstance(other, Clicked) and self.tile == other.tile

class Zero:
    def __init__(self, tile):
        self.tile = tile

    def __eq__(self, other):
        return isinstance(other, Zero) and self.tile == other.tile

class One:
    def __init__(self, tile):
        self.tile = tile

    def __eq__(self, other):
        return isinstance(other, One) and self.tile == other.tile

class Two:
    def __init__(self, tile):
        self.tile = tile

    def __eq__(self, other):
        return isinstance(other, Two) and self.tile == other.tile

class Three:
    def __init__(self, tile):
        self.tile = tile

    def __eq__(self, other):
        return isinstance(other, Three) and self.tile == other.tile

class Sat:
    def __init__(self, tile):
        self.tile = tile

    def __eq__(self, other):
        return isinstance(other, Sat) and self.tile == other.tile

class Mine:
    def __init__(self, tile):
        self.tile = tile

    def __eq__(self, other):
        return isinstance(other, Mine) and self.tile == other.tile

class Diff():
    def __init__(self, tile1, tile2):
    	self.tile1 = tile1
    	self.tile2 = tile2

    def __eq__(self, other):
    	return isinstance(other, Diff) and self.tile1 == other.tile1 and self.tile2 == other.tile2

class Adj():
    def __init__(self, tile1, tile2):
        self.tile1 = tile1
        self.tile2 = tile2

     def __eq__(self, other):
        return isinstance(other, Adj) and self.tile1 == other.tile1 and self.tile2 == other.tile2

class AdjMine():
	def __init__(self, tile1, tile2):
    	self.tile1 = tile1
    	self.tile2 = tile2

     def __eq__(self, other):
    	return isinstance(other, AdjMine) and self.tile1 == other.tile1 and self.tile2 == other.tile2

class AdjClicked():
	def __init__(self, tile1, tile2):
    	self.tile1 = tile1
    	self.tile2 = tile2

     def __eq__(self, other):
    	return isinstance(other, AdjClicked) and self.tile1 == other.tile1 and self.tile2 == other.tile2

class NumAdj():
	def __init__(self, tile):
    	self.tile = tile

     def __eq__(self, other):
    	return isinstance(other, NumAdj) and self.tile == other.tile

class NumAdjMines():
	def __init__(self, tile):
    	self.tile = tile

     def __eq__(self, other):
    	return isinstance(other, NumAdjMines) and self.tile == other.tile

class NumAdjClicked():
	def __init__(self, tile):
    	self.tile = tile

     def __eq__(self, other):
    	return isinstance(other, NumAdjClicked) and self.tile == other.tile


