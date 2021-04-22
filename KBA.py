import random
from Predicates import *
from Rule import Rule

'''A class representing a Knowledge-Based Agent (KBA) for the Minesweeper game.
'''
class KBA:
	'''Constructor for the KBA, which initializes the knowledge base (KB).
	The KB consists of two dictionaries: one containing facts (atomic sentences) and another containing rules (Horn clauses) 
	'''
	def __init__(self, size):
		self.board_size = size
		self.facts = {}
		self.rules = {}
		self.init_facts()
		self.init_rules()

	'''Chooses an action (a tile to click) to take based on the given board state and the KB.
	:param board: (2D array) the current board state
	:return: (tuple) the tile to click
	'''
	def get_action(self, board):
		tile = self.get_unclicked_known_not_mine_tile(board)

		if tile is None:
			tile = self.get_unclicked_not_known_mine_tile(board)
		
		if tile is None:
			tile = self.get_unclicked_random_tile(board)

		return tile

	'''Gets the first unclicked tile which is known not to be a mine.
	:param board: (2D array) the current board state
	:return: (tuple) the known non-mine
	'''
	def get_unclicked_known_not_mine_tile(self, board):
		for i in range(self.board_size):
			for j in range(self.board_size):
				if not board[i][j].clicked and self.prove((Preds.NOT_MINE, i, j)):
					return (i, j)

		return None

	'''Gets the first unclicked tile which is not known to be a mine.
	:param board: (2D array) the current board state
	:return: (tuple) the potential non-mine
	'''
	def get_unclicked_not_known_mine_tile(self, board):
		unknown = []
		for i in range(self.board_size):
			for j in range(self.board_size):
				if not board[i][j].clicked and not self.prove((Preds.MINE, i, j)):
					unknown.append((i, j))

		return random.choice(unknown) if len(unknown) > 0 else None

	'''Gets a random unclicked tile.
	:param board: (2D array) the current board state
	:return: (tuple) the tile chosen
	'''
	def get_unclicked_random_tile(self, board):
		found = False
		while not found:
			i, j = random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)
			if not board[i][j].clicked:
				found = True

		return i, j

	'''Adds new information to the KB regarding the given number that was seen in the given tile.
	:param row: (int) the row of the perceived tile
	:param col: (int) the column of the perceived tile
	:param number: (int) the number in the percieved tile
	'''
	def tell(self, row, col, number):
		if number == 0:
			self.record_percept((Preds.ZERO, row, col))

		elif number == 1:
			self.record_percept((Preds.ONE, row, col))

		elif number == 2:
			self.record_percept((Preds.TWO, row, col))

		elif number == 3:
			self.record_percept((Preds.THREE, row, col))

	'''Records a new percept, which consists of two steps:
		(1) Adding the number in the newly perceived tile to the KB and 
		(2) Removing the fact stating that the tile was unclicked as that is no longer true.
	:param sentence: (tuple) the new sentence 
	'''
	def record_percept(self, sentence):
		pred, i, j = sentence
		self.add_to_KB(sentence)
		self.facts[Preds.UNCLICKED].remove((i, j))

	'''Adds the given sentence to the KB.
	:param sentence: (tuple) the sentence to add
	'''
	def add_to_KB(self, sentence):
		if sentence[0] != 'not':
			pred, i, j = sentence
			if pred not in self.facts.keys():
				self.facts[pred] = []

			if (i, j) not in self.facts[pred]:
				self.facts[pred].append((i, j))

	'''Initializes the facts portion of the KB.
	It does so by adding an atomic sentence stating that each tile is unclicked.
	'''
	def init_facts(self):
		self.facts[Preds.UNCLICKED] = []
		for i in range(self.board_size):
			for j in range(self.board_size):
				self.facts[Preds.UNCLICKED].append((i,j))

	'''Initializes the rules portion of the KB.
	It does so by propositionalizing the given rules.
	'''
	def init_rules(self):
		self.rules[Preds.NOT_MINE] = []
		self.rules[Preds.SAT] = []
		self.rules[Preds.UNSAT] = []
		self.rules[Preds.MINE] = []
		for i in range(self.board_size):
			for j in range(self.board_size):
				adjacent_tiles = self.get_adjacent_tiles((i, j))

				for k, l in adjacent_tiles:
					self.rules[Preds.NOT_MINE].append(Rule(lhs=[(Preds.SAT, k, l), ('not', Preds.MINE, i, j)], rhs=(Preds.NOT_MINE, i, j)))
				
				self.rules[Preds.SAT].append(Rule(lhs=[(Preds.ZERO, i, j)], rhs=(Preds.SAT, i, j)))

				count = (Preds.COUNT, )
				for k, l in adjacent_tiles:
					count += ((Preds.MINE, k, l), )
				self.rules[Preds.SAT].append(Rule(lhs=[(Preds.ONE, i, j), (Preds.EQUAL, 1, count)], rhs=(Preds.SAT, i, j)))
				count = (Preds.COUNT, )
				for k, l in adjacent_tiles:
					count += ((Preds.MINE, k, l), )
				self.rules[Preds.SAT].append(Rule(lhs=[(Preds.TWO, i, j), (Preds.EQUAL, 2, count)], rhs=(Preds.SAT, i, j)))
				count = (Preds.COUNT, )
				for k, l in adjacent_tiles:
					count += ((Preds.MINE, k, l), )
				self.rules[Preds.SAT].append(Rule(lhs=[(Preds.THREE, i, j), (Preds.EQUAL, 3, count)], rhs=(Preds.SAT, i, j)))
								
				for k, l in adjacent_tiles:
					count = (Preds.COUNT, )
					adjacent_tiles2 = self.get_adjacent_tiles((k, l))
					for m, n in adjacent_tiles2:
						count += ((Preds.UNCLICKED, m, n), )
					self.rules[Preds.MINE].append(Rule(lhs=[(Preds.UNCLICKED, i, j), (Preds.ONE, k, l), (Preds.EQUAL, 1, count)], rhs=(Preds.MINE, i, j)))
				
				for k, l in adjacent_tiles:
					count = (Preds.COUNT, )
					adjacent_tiles2 = self.get_adjacent_tiles((k, l))
					for m, n in adjacent_tiles2:
						count += ((Preds.UNCLICKED, m, n), )
					self.rules[Preds.MINE].append(Rule(lhs=[(Preds.UNCLICKED, i, j), (Preds.TWO, k, l), (Preds.EQUAL, 2, count)], rhs=(Preds.MINE, i, j)))
				
				for k, l in adjacent_tiles:
					count = (Preds.COUNT, )
					adjacent_tiles2 = self.get_adjacent_tiles((k, l))
					for m, n in adjacent_tiles2:
						count += ((Preds.UNCLICKED, m, n), )
					self.rules[Preds.MINE].append(Rule(lhs=[(Preds.UNCLICKED, i, j), (Preds.THREE, k, l), (Preds.EQUAL, 3, count)], rhs=(Preds.MINE, i, j)))

	'''Gets the set of adjacent tiles to the given tile
	:param tile: (tuple) the tile whose adjacent tiles are desired
	:return: (list) the adjacent tiles
	'''
	def get_adjacent_tiles(self, tile):
		i, j = tile
		adj = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
		result = []
		for k, l in adj:
			if not (k < 0 or k >= self.board_size or l < 0 or l >= self.board_size):
				result.append((k, l))

		return result

	'''Proves the given sentence if it can.
	:param sentence: (tuple) the sentence to be proven
	:return: (boolean) True if the sentence is entailed by the KB, False otherwise
	'''
	def prove(self, sentence):
		if sentence[0] == 'not':
			return not self.prove(sentence[1:])

		pred = sentence[0]

		# the only hope for these things is if they're in the KB because there's no rules to prove
		if pred in [Preds.ZERO, Preds.ONE, Preds.TWO, Preds.THREE, Preds.UNCLICKED]:
			return self.fact_check(sentence)

		# these could be in the KB, but we could prove them if necessary 
		elif pred in [Preds.SAT, Preds.UNSAT, Preds.MINE, Preds.NOT_MINE]:
			return self.fact_check(sentence) or self.backward_chain(sentence)

		# these predicates get handled specially
		elif pred == Preds.EQUAL:
			x, y = sentence[1], sentence[2]
			return self.equal(x, y)
				
		# elif pred == Preds.NOT_EQUAL:
		# 	x, y = sentence[1], sentence[2]
		# 	return self.not_equal(x, y)
				
		elif pred == Preds.COUNT:
			return self.count(sentence[1:])

		else:
			print("That's an illegal predicate silly :(")
			return False

	'''Checks to see if the given fact is in the facts portion of the KB or not.
	:param fact: (tuple) the fact to check
	:return: (boolean) True if the fact is in the KB, False otherwise
	'''
	def fact_check(self, fact):
		pred, i, j = fact
		if pred in self.facts.keys() and (i, j) in self.facts[pred]:
			return True
		else:
			return False

	'''Performs backward chaining in an attempt to find a proof for the given sentence.
	Adds any newly derived knowledge to the KB.
	:param sentence: (tuple) the sentence to prove
	:return: (boolean) True if the sentence is entailed by the KB, False otherwise
	'''
	def backward_chain(self, sentence):
		rules = self.get_rules(sentence)
		for r in rules:
			provable = True
			for conjunct in r.lhs:
				if provable:
					result = self.prove(conjunct)
					if result:
						self.add_to_KB(conjunct)
					else:
						provable = False

			# case: we were able to prove all the conjuncts for the rule!
			if provable:
				self.add_to_KB(sentence)
				return True

		return False

	'''Gets a list of rules from the KB which could potentially be used to prove the given sentence, 
	i.e. the given sentence is the consequent of the rule
	:param sentence: (tuple) the sentence whose rules are desired
	:return: (list) the rules
	'''
	def get_rules(self, sentence):
		pred, i, j = sentence
		rules = []
		if pred in self.rules.keys():
			for r in self.rules[pred]:
				if sentence == r.rhs:
					rules.append(r)

		return rules

	'''Function to evaluate the function symbol EQUAL.
	:param x: one of the items to compare
	:param y: the other item to compare
	:return: (boolean) True if x and y are equal, False otherwise
	'''
	def equal(self, x, y):
		if not isinstance(x, int):
			x = self.prove(x)
		if not isinstance(y, int):
			y = self.prove(y)

		return x == y

	# def not_equal(self, x, y):
	# 	if not isinstance(x, int):
	# 		x = self.prove(x)
	# 	if not isinstance(y, int):
	# 		y = self.prove(y)

	# 	return x != y

	'''Funtion to evaluate the function symbol COUNT.
	:param inputs: (list) the items over which to count
	:return: (int) the number of items in inputs which evaluate to true
	'''
	def count(self, inputs):
		count = 0
		for i in inputs:
			if self.prove(i):
				count += 1

		return count
