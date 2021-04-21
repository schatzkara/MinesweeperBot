import random
from Predicates import *
from Rule import Rule


class KBA:
	def __init__(self, size):
		self.board_size = size
		self.facts = {}
		self.rules = {}
		self.init_facts()
		self.init_rules()

	def get_action(self, board):
		tile = self.get_known_not_mine_tile(board)

		if tile is None:
			tile = self.get_not_known_mine_tile(board)
		
		if tile is None:
			tile = self.get_random_unclicked_tile(board)

		return tile

	def get_known_not_mine_tile(self, board):
		for i in range(self.board_size):
			for j in range(self.board_size):
				if not board[i][j].clicked and self.prove((Preds.NOT_MINE, i, j)):
					return (i, j)

		return None

	def get_not_known_mine_tile(self, board):
		unknown = []
		for i in range(self.board_size):
			for j in range(self.board_size):
				if not board[i][j].clicked and not self.prove((Preds.MINE, i, j)):
					unknown.append((i, j))

		return random.choice(unknown) if len(unknown) > 0 else None

	def get_random_unclicked_tile(self, board):
		found = False
		while not found:
			i, j = random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)
			if not board[i][j].clicked:
				found = True

		return i, j

	def tell(self, row, col, number):
		if number == 0:
			self.record_percept((Preds.ZERO, row, col))

		elif number == 1:
			self.record_percept((Preds.ONE, row, col))

		elif number == 2:
			self.record_percept((Preds.TWO, row, col))

		elif number == 3:
			self.record_percept((Preds.THREE, row, col))

	
	def record_percept(self, sentence):
		pred, i, j = sentence
		self.add_to_KB(sentence)
		self.facts[Preds.UNCLICKED].remove((i, j))

	def add_to_KB(self, sentence):
		if sentence[0] != 'not':
			pred, i, j = sentence
			if pred not in self.facts.keys():
				self.facts[pred] = []

			if (i, j) not in self.facts[pred]:
				self.facts[pred].append((i, j))

	def init_facts(self):
		self.facts[Preds.UNCLICKED] = []
		for i in range(self.board_size):
			for j in range(self.board_size):
				self.facts[Preds.UNCLICKED].append((i,j))

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

	def get_adjacent_tiles(self, tile):
		i, j = tile
		adj = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)]
		result = []
		for k, l in adj:
			if not (k < 0 or k >= self.board_size or l < 0 or l >= self.board_size):
				result.append((k, l))

		return result

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
				
		elif pred == Preds.NOT_EQUAL:
			x, y = sentence[1], sentence[2]
			return self.not_equal(x, y)
				
		elif pred == Preds.COUNT:
			return self.count(sentence[1:])

		else:
			print("That's an illegal predicate silly :(")
			return False

	def fact_check(self, fact):
		pred, i, j = fact
		if pred in self.facts.keys() and (i, j) in self.facts[pred]:
			return True
		else:
			return False

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

	def get_rules(self, sentence):
		pred, i, j = sentence
		rules = []
		if pred in self.rules.keys():
			for r in self.rules[pred]:
				if sentence == r.rhs:
					rules.append(r)

		return rules

	def equal(self, x, y):
		if not isinstance(x, int):
			x = self.prove(x)
		if not isinstance(y, int):
			y = self.prove(y)

		return x == y

	def not_equal(self, x, y):
		if not isinstance(x, int):
			x = self.prove(x)
		if not isinstance(y, int):
			y = self.prove(y)

		return x != y

	def count(self, inputs):
		count = 0
		for i in inputs:
			if self.prove(i):
				count += 1

		return count
