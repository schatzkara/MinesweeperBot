



class Diff():
    def __init__(self, tile1, tile2):
    	self.tile1 = tile1
    	self.tile2 = tile2

    def __eq__(self, other):
    	return isinstance(other, Diff) and self.tile1 == other.tile1 and self.tile2 == other.tile2


class AdjMine():
	def __init__(self, tile1, tile2):
    	self.tile1 = tile1
    	self.tile2 = tile2

     def __eq__(self, other):
    	return isinstance(other, AdjMine) and self.tile1 == other.tile1 and self.tile2 == other.tile2

class Adj():
	def __init__(self, tile1, tile2):
    	self.tile1 = tile1
    	self.tile2 = tile2

     def __eq__(self, other):
    	return isinstance(other, Adj) and self.tile1 == other.tile1 and self.tile2 == other.tile2

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


