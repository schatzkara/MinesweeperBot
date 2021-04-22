from Constants import *
from enum import Enum

class Preds(Enum):
	ZERO = 0
	ONE = 1
	TWO = 2
	THREE = 3
	UNCLICKED = 4
	SAT = 5
	UNSAT = 6
	MINE = 7
	NOT_MINE = 8
	EQUAL = 9
	# NOT_EQUAL = 10
	COUNT = 10

def sat(tile, number, mines):
	return number == num_adj_mine(tile, mines)

def mine(tile, facts):
	adjacent = adj_tiles(tile)

	for adj_tile in adjacent:
		if not sat(adj_tile):
			if adj_tile in facts[Predicates.ONE]:
				number = 1
			if adj_tile in facts[Predicates.TWO]:
				number = 2
			if adj_tile in facts[Predicates.THREE]:
				number = 3

			if number == num_adj(adj_tile) - adj_clicked(adj_clicked):
				return True

	return False

def not_mine(tile):
	adjacent = adj_tiles(tile)

	for adj_tile in adjacent:
		if sat(adj_tile):
			return True

	return False

def diff(tile1, tile2):
	return self.tile1 != self.tile2

def adj_tiles(tile):
	i, j = tile
	return [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]

def adj(tile1, tile2):
	i, j = tile1
	k, l = tile2
	if i == k:
		if j == l - 1:
			return True
		if j == l + 1:
			return True
	if j == l:
		if i == k - 1:
			return True
		if i == k + 1:
			return True

	return False

def adj_mine(tile1, tile2, mines):
	return adj(tile1, tile2) and tile1 in mines

def adj_clicked(tile1, tile2, clicked):
	return adj(tile1, tile2) and tile1 in clicked

def num_adj(tile):
	i, j = tile
	if (i == 0 or i == BOARD_SIZE-1) and (j == 0 or j == BOARD_SIZE-1):
		return 3

	if ((i == 0 or i == BOARD_SIZE-1) and j != 0 and j != BOARD_SIZE-1):
		return 5

	if i != 0 and i != BOARD_SIZE-1 and j != 0 and j != BOARD_SIZE-1:
		return 8

	print('bad tile')

def num_adj_mines(tile, mines):
	adjacent = adj_tiles(tile)

	count = 0
	for adj_tile in adjacent:
		if adj_tile in mines:
			count += 1

	return count

def num_adj_clicked(tile, clicked):
	adjacent = adj_tiles(tile)

	count = 0
	for adj_tile in adjacent:
		if adj_tile in clicked:
			count += 1

	return count

# class Clicked:
#     def __init__(self, tile):
#         self.tile = tile
#         self.predicate = Predicates.CLICKED

#     def __eq__(self, other):
#         return isinstance(other, Clicked) and self.tile == other.tile

# class Zero:
#     def __init__(self, tile):
#         self.tile = tile
#         self.predicate = Predicates.ZERO

#     def __eq__(self, other):
#         return isinstance(other, Zero) and self.tile == other.tile

# class One:
#     def __init__(self, tile):
#         self.tile = tile
#         self.predicate = Predicates.ONE

#     def __eq__(self, other):
#         return isinstance(other, One) and self.tile == other.tile

# class Two:
#     def __init__(self, tile):
#         self.tile = tile
#         self.predicate = Predicates.TWO

#     def __eq__(self, other):
#         return isinstance(other, Two) and self.tile == other.tile

# class Three:
#     def __init__(self, tile):
#         self.tile = tile
#         self.predicate = Predicates.THREE

#     def __eq__(self, other):
#         return isinstance(other, Three) and self.tile == other.tile

# class Sat:
#     def __init__(self, tile):
#         self.tile = tile
#         self.predicate = Predicates.SAT

#     def __eq__(self, other):
#         return isinstance(other, Sat) and self.tile == other.tile

# class Mine:
#     def __init__(self, tile):
#         self.tile = tile
#         self.predicate = Predicates.MINE

#     def __eq__(self, other):
#         return isinstance(other, Mine) and self.tile == other.tile

# class Diff():
#     def __init__(self, tile1, tile2):
#     	self.tile1 = tile1
#     	self.tile2 = tile2
#         self.predicate = Predicates.DIFF

#     def value(self):
#         return self.tile1 != self.tile2

#     def __eq__(self, other):
#     	return isinstance(other, Diff) and self.tile1 == other.tile1 and self.tile2 == other.tile2

# class Adj():
#     def __init__(self, tile1, tile2):
#         self.tile1 = tile1
#         self.tile2 = tile2
#         self.predicate = Predicates.ADJ

#      def __eq__(self, other):
#         return isinstance(other, Adj) and self.tile1 == other.tile1 and self.tile2 == other.tile2

# class AdjMine():
# 	def __init__(self, tile1, tile2):
#     	self.tile1 = tile1
#     	self.tile2 = tile2
#         self.predicate = Predicates.ADJ_MINE

#      def __eq__(self, other):
#     	return isinstance(other, AdjMine) and self.tile1 == other.tile1 and self.tile2 == other.tile2

# class AdjClicked():
# 	def __init__(self, tile1, tile2):
#     	self.tile1 = tile1
#     	self.tile2 = tile2
#         self.predicate = Predicates.ADJ_CLICKED

#      def __eq__(self, other):
#     	return isinstance(other, AdjClicked) and self.tile1 == other.tile1 and self.tile2 == other.tile2

# class NumAdj():
# 	def __init__(self):
#     	# self.tile = tile
#         self.predicate = Predicates.NUM_ADJ

#     def value(self, tile):
#         i, j = tile
#         if (i == 0 or i == BOARD_SIZE-1) and (j == 0 or j == BOARD_SIZE-1):
#             return 3

#         if ((i == 0 or i == BOARD_SIZE-1) and j != 0 and j != BOARD_SIZE-1):
#             return 5

#         if i != 0 and i != BOARD_SIZE-1 and j != 0 and j != BOARD_SIZE-1:
#             return 8

#      def __eq__(self, other):
#     	return isinstance(other, NumAdj) and self.tile == other.tile

# class NumAdjMines():
# 	def __init__(self):
#     	# self.tile = tile
#         self.predicate = Predicates.NUM_ADJ_MINES

#     def value(self, tile, board, KB):
#         i, j = tile
#         adjacent = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
#         mines = KB[Predicates.MINE]

#         count = 0
#         for adj_tile in adjacent:
#             for m in mines:
#                 if m.tile == adj_tile:
#                     count += 1

#         return count

#     def __eq__(self, other):
#     	return isinstance(other, NumAdjMines) and self.tile == other.tile

# class NumAdjClicked():
# 	def __init__(self):
#     	# self.tile = tile
#         self.predicate = Predicates.NUM_ADJ_CLICKED

#     def value(self, tile, board, KB):
#         i, j = tile
#         adjacent = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
#         clicked = KB[Predicates.CLICKED]

#         count = 0
#         for adj_tile in adjacent:
#             for c in clicked:
#                 if c.tile == adj_tile:
#                     count += 1

#         return count

#     def __eq__(self, other):
#     	return isinstance(other, NumAdjClicked) and self.tile == other.tile

# def equals(i, j):
#     return i == j