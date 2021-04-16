import random
from Predicates import *


class KBA:
	def __init__(self, size):
		self.board_size = size
		self.facts = {}
		self.rules = {}

	def get_action(self):
		for i in range(self.board_size):
			for j in range(self.board_size):
				if self.prove((Preds.NOT_MINE, i, j)):
					return (i, j)

		return (random.rand_int(self.board_size), random.rand_int(self.board_size))

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
		pred, i, j
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
		for i in range(self.board_size):
			for j in range(self.board_size):
				self.rules[Preds.NOT_MINE] = Rule(lhs=[(Preds.SAT, i-1, j-1)], rhs=(Preds.NOT_MINE, i, j))
				self.rules[Preds.NOT_MINE] = Rule(lhs=[(Preds.SAT, i-1, j)], rhs=(Preds.NOT_MINE, i, j))
				self.rules[Preds.NOT_MINE] = Rule(lhs=[(Preds.SAT, i-1, j+1)], rhs=(Preds.NOT_MINE, i, j))
				self.rules[Preds.NOT_MINE] = Rule(lhs=[(Preds.SAT, i, j-1)], rhs=(Preds.NOT_MINE, i, j))
				self.rules[Preds.NOT_MINE] = Rule(lhs=[(Preds.SAT, i, j+1)], rhs=(Preds.NOT_MINE, i, j))
				self.rules[Preds.NOT_MINE] = Rule(lhs=[(Preds.SAT, i+1, j-1)], rhs=(Preds.NOT_MINE, i, j))
				self.rules[Preds.NOT_MINE] = Rule(lhs=[(Preds.SAT, i+1, j)], rhs=(Preds.NOT_MINE, i, j))
				self.rules[Preds.NOT_MINE] = Rule(lhs=[(Preds.SAT, i+1, j+1)], rhs=(Preds.NOT_MINE, i, j))

				self.rules[Preds.SAT] = Rule(lhs=[(Preds.ZERO, i, j)], rhs=(Preds.SAT, i, j))
				self.rules[Preds.SAT] = Rule(lhs=[(Preds.ONE, i, j), (Preds.EQUAL, 1, (Preds.COUNT, (Preds.MINE, i-1, j-1), (Preds.MINE, i-1, j), (Preds.MINE, i-1, j+1), (Preds.MINE, i, j-1), (Preds.MINE, i, j+1), (Preds.MINE, i+1, j-1), (Preds.MINE, i+1, j), (Preds.MINE, i+1, j+1)))], rhs=(Preds.SAT, i, j))
				self.rules[Preds.SAT] = Rule(lhs=[(Preds.TWO, i, j), (Preds.EQUAL, 2, (Preds.COUNT, (Preds.MINE, i-1, j-1), (Preds.MINE, i-1, j), (Preds.MINE, i-1, j+1), (Preds.MINE, i, j-1), (Preds.MINE, i, j+1), (Preds.MINE, i+1, j-1), (Preds.MINE, i+1, j), (Preds.MINE, i+1, j+1)))], rhs=(Preds.SAT, i, j))
				self.rules[Preds.SAT] = Rule(lhs=[(Preds.THREE, i, j), (Preds.EQUAL, 3, (Preds.COUNT, (Preds.MINE, i-1, j-1), (Preds.MINE, i-1, j), (Preds.MINE, i-1, j+1), (Preds.MINE, i, j-1), (Preds.MINE, i, j+1), (Preds.MINE, i+1, j-1), (Preds.MINE, i+1, j), (Preds.MINE, i+1, j+1)))], rhs=(Preds.SAT, i, j))

				self.rules[Preds.UNSAT] = Rule(lhs=[(Preds.ONE, i, j), (Preds.NOT_EQUAL, 1, (Preds.COUNT, (Preds.MINE, i-1, j-1), (Preds.MINE, i-1, j), (Preds.MINE, i-1, j+1), (Preds.MINE, i, j-1), (Preds.MINE, i, j+1), (Preds.MINE, i+1, j-1), (Preds.MINE, i+1, j), (Preds.MINE, i+1, j+1)))], rhs=(Preds.SAT, i, j))
				self.rules[Preds.UNSAT] = Rule(lhs=[(Preds.TWO, i, j), (Preds.NOT_EQUAL, 2, (Preds.COUNT, (Preds.MINE, i-1, j-1), (Preds.MINE, i-1, j), (Preds.MINE, i-1, j+1), (Preds.MINE, i, j-1), (Preds.MINE, i, j+1), (Preds.MINE, i+1, j-1), (Preds.MINE, i+1, j), (Preds.MINE, i+1, j+1)))], rhs=(Preds.SAT, i, j))
				self.rules[Preds.UNSAT] = Rule(lhs=[(Preds.THREE, i, j), (Preds.NOT_EQUAL, 3, (Preds.COUNT, (Preds.MINE, i-1, j-1), (Preds.MINE, i-1, j), (Preds.MINE, i-1, j+1), (Preds.MINE, i, j-1), (Preds.MINE, i, j+1), (Preds.MINE, i+1, j-1), (Preds.MINE, i+1, j), (Preds.MINE, i+1, j+1)))], rhs=(Preds.SAT, i, j))

				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i-1, j-1), (Preds.ONE, i-1, j-1), (Preds.EQUAL, 1, (Preds.COUNT, (Preds.UNCLICKED, i-2, j-2), (Preds.UNCLICKED, i-2, j-1), (Preds.UNCLICKED, i-2, j), (Preds.UNCLICKED, i-1, j-2), (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i, j-2), (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i-1, j), (Preds.ONE, i-1, j), (Preds.EQUAL, 1, (Preds.COUNT, (Preds.UNCLICKED, i-2, j-1), (Preds.UNCLICKED, i-2, j), (Preds.UNCLICKED, i-2, j+1), (Preds.UNCLICKED, i-1, j-1), (Preds.UNCLICKED, i-1, j+1), (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i-1, j+1), (Preds.ONE, i-1, j+1), (Preds.EQUAL, 1, (Preds.COUNT, (Preds.UNCLICKED, i-2, j), (Preds.UNCLICKED, i-2, j+1), (Preds.UNCLICKED, i-2, j+2), (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i-1, j+2), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1), (Preds.UNCLICKED, i, j+2)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i, j-1), (Preds.ONE, i, j-1), (Preds.EQUAL, 1, (Preds.COUNT, (Preds.UNCLICKED, i-1, j-2), (Preds.UNCLICKED, i-1, j-1), (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i, j-2), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i+1, j-2), (Preds.UNCLICKED, i+1, j-1), (Preds.UNCLICKED, i+1, j)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i, j+1), (Preds.ONE, i, j+1), (Preds.EQUAL, 1, (Preds.COUNT, (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i-1, j+1), (Preds.UNCLICKED, i-1, j+2), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+2), (Preds.UNCLICKED, i+1, j), (Preds.UNCLICKED, i+1, j+1), (Preds.UNCLICKED, i+1, j+2)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i+1, j-1), (Preds.ONE, i+1, j-1), (Preds.EQUAL, 1, (Preds.COUNT, (Preds.UNCLICKED, i, j-2), (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i+1, j-2), (Preds.UNCLICKED, i+1, j), (Preds.UNCLICKED, i+2, j-2), (Preds.UNCLICKED, i+2, j-1), (Preds.UNCLICKED, i+2, j)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i+1, j), (Preds.ONE, i+1, j), (Preds.EQUAL, 1, (Preds.COUNT, (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1), (Preds.UNCLICKED, i+1, j-1), (Preds.UNCLICKED, i+1, j+1), (Preds.UNCLICKED, i+2, j-1), (Preds.UNCLICKED, i+2, j), (Preds.UNCLICKED, i+2, j+1)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i+1, j+1), (Preds.ONE, i+1, j+1), (Preds.EQUAL, 1, (Preds.COUNT, (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1), (Preds.UNCLICKED, i, j+2), (Preds.UNCLICKED, i+1, j), (Preds.UNCLICKED, i+1, j+2), (Preds.UNCLICKED, i+2, j), (Preds.UNCLICKED, i+2, j+1), (Preds.UNCLICKED, i+2, j+2)))], rhs=(Preds.MINE, i, j))

				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i-1, j-1), (Preds.TWO, i-1, j-1), (Preds.EQUAL, 2, (Preds.COUNT, (Preds.UNCLICKED, i-2, j-2), (Preds.UNCLICKED, i-2, j-1), (Preds.UNCLICKED, i-2, j), (Preds.UNCLICKED, i-1, j-2), (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i, j-2), (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i-1, j), (Preds.TWO, i-1, j), (Preds.EQUAL, 2, (Preds.COUNT, (Preds.UNCLICKED, i-2, j-1), (Preds.UNCLICKED, i-2, j), (Preds.UNCLICKED, i-2, j+1), (Preds.UNCLICKED, i-1, j-1), (Preds.UNCLICKED, i-1, j+1), (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i-1, j+1), (Preds.TWO, i-1, j+1), (Preds.EQUAL, 2, (Preds.COUNT, (Preds.UNCLICKED, i-2, j), (Preds.UNCLICKED, i-2, j+1), (Preds.UNCLICKED, i-2, j+2), (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i-1, j+2), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1), (Preds.UNCLICKED, i, j+2)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i, j-1), (Preds.TWO, i, j-1), (Preds.EQUAL, 2, (Preds.COUNT, (Preds.UNCLICKED, i-1, j-2), (Preds.UNCLICKED, i-1, j-1), (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i, j-2), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i+1, j-2), (Preds.UNCLICKED, i+1, j-1), (Preds.UNCLICKED, i+1, j)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i, j+1), (Preds.TWO, i, j+1), (Preds.EQUAL, 2, (Preds.COUNT, (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i-1, j+1), (Preds.UNCLICKED, i-1, j+2), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+2), (Preds.UNCLICKED, i+1, j), (Preds.UNCLICKED, i+1, j+1), (Preds.UNCLICKED, i+1, j+2)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i+1, j-1), (Preds.TWO, i+1, j-1), (Preds.EQUAL, 2, (Preds.COUNT, (Preds.UNCLICKED, i, j-2), (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i+1, j-2), (Preds.UNCLICKED, i+1, j), (Preds.UNCLICKED, i+2, j-2), (Preds.UNCLICKED, i+2, j-1), (Preds.UNCLICKED, i+2, j)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i+1, j), (Preds.TWO, i+1, j), (Preds.EQUAL, 2, (Preds.COUNT, (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1), (Preds.UNCLICKED, i+1, j-1), (Preds.UNCLICKED, i+1, j+1), (Preds.UNCLICKED, i+2, j-1), (Preds.UNCLICKED, i+2, j), (Preds.UNCLICKED, i+2, j+1)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i+1, j+1), (Preds.TWO, i+1, j+1), (Preds.EQUAL, 2, (Preds.COUNT, (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1), (Preds.UNCLICKED, i, j+2), (Preds.UNCLICKED, i+1, j), (Preds.UNCLICKED, i+1, j+2), (Preds.UNCLICKED, i+2, j), (Preds.UNCLICKED, i+2, j+1), (Preds.UNCLICKED, i+2, j+2)))], rhs=(Preds.MINE, i, j))

				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i-1, j-1), (Preds.THREE, i-1, j-1), (Preds.EQUAL, 3, (Preds.COUNT, (Preds.UNCLICKED, i-2, j-2), (Preds.UNCLICKED, i-2, j-1), (Preds.UNCLICKED, i-2, j), (Preds.UNCLICKED, i-1, j-2), (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i, j-2), (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i-1, j), (Preds.THREE, i-1, j), (Preds.EQUAL, 3, (Preds.COUNT, (Preds.UNCLICKED, i-2, j-1), (Preds.UNCLICKED, i-2, j), (Preds.UNCLICKED, i-2, j+1), (Preds.UNCLICKED, i-1, j-1), (Preds.UNCLICKED, i-1, j+1), (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i-1, j+1), (Preds.THREE, i-1, j+1), (Preds.EQUAL, 3, (Preds.COUNT, (Preds.UNCLICKED, i-2, j), (Preds.UNCLICKED, i-2, j+1), (Preds.UNCLICKED, i-2, j+2), (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i-1, j+2), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1), (Preds.UNCLICKED, i, j+2)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i, j-1), (Preds.THREE, i, j-1), (Preds.EQUAL, 3, (Preds.COUNT, (Preds.UNCLICKED, i-1, j-2), (Preds.UNCLICKED, i-1, j-1), (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i, j-2), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i+1, j-2), (Preds.UNCLICKED, i+1, j-1), (Preds.UNCLICKED, i+1, j)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i, j+1), (Preds.THREE, i, j+1), (Preds.EQUAL, 3, (Preds.COUNT, (Preds.UNCLICKED, i-1, j), (Preds.UNCLICKED, i-1, j+1), (Preds.UNCLICKED, i-1, j+2), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+2), (Preds.UNCLICKED, i+1, j), (Preds.UNCLICKED, i+1, j+1), (Preds.UNCLICKED, i+1, j+2)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i+1, j-1), (Preds.THREE, i+1, j-1), (Preds.EQUAL, 3, (Preds.COUNT, (Preds.UNCLICKED, i, j-2), (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i+1, j-2), (Preds.UNCLICKED, i+1, j), (Preds.UNCLICKED, i+2, j-2), (Preds.UNCLICKED, i+2, j-1), (Preds.UNCLICKED, i+2, j)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i+1, j), (Preds.THREE, i+1, j), (Preds.EQUAL, 3, (Preds.COUNT, (Preds.UNCLICKED, i, j-1), (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1), (Preds.UNCLICKED, i+1, j-1), (Preds.UNCLICKED, i+1, j+1), (Preds.UNCLICKED, i+2, j-1), (Preds.UNCLICKED, i+2, j), (Preds.UNCLICKED, i+2, j+1)))], rhs=(Preds.MINE, i, j))
				self.rules[Preds.MINE] = Rule(lhs=[(Preds.UNSAT, i+1, j+1), (Preds.THREE, i+1, j+1), (Preds.EQUAL, 3, (Preds.COUNT, (Preds.UNCLICKED, i, j), (Preds.UNCLICKED, i, j+1), (Preds.UNCLICKED, i, j+2), (Preds.UNCLICKED, i+1, j), (Preds.UNCLICKED, i+1, j+2), (Preds.UNCLICKED, i+2, j), (Preds.UNCLICKED, i+2, j+1), (Preds.UNCLICKED, i+2, j+2)))], rhs=(Preds.MINE, i, j))

	def prove(self, sentence):
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
		if (i, j) in self.facts[pred]:
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
		for r in self.rules[pred]:
			if sentence == r.rhs:
				rules.add(r)

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


	# def substitute(self, substitutions, sentence):


	# def unify(self, sentence1, sentence2, substitution):
		'''if substitution == None:
			return None
		elif sentence1 == sentence2:
			return substitution
		elif self.is_variable(sentence1):
			return unify_var(sentence1, sentence2, substitution)
		elif self.is_variable(sentence2):
			return unify_var(sentence2, sentence1, substitution)
		elif self.is_compound(x) and self.is_compound(y):
			return unify(x.)'''


	# def standardize_variables(self, sentence):

'''
	def forward_chaining(self, goal):
		first_iteration = true
		while first_iteration or len(new) == 0:
			new = {}
			for r in self.rules:
				r = standardize_variables(r)
				for 
'''
	# def unify_var(self, variable1, variable2):


	# def is_variable(self, sentence):


	# def is_compound(self, sentence):


	# def fetch_rules(self, goal):


	# def prioritize_goals(self, goals):


	# def BC_OR(self, goal, substitution):
	# 	rules = self.fetch_rules(goal)
	# 	for r in rules:
	# 		r = standardize_variables(r)

	# 		subs = self.BC_AND(r.lhs, self.unify(r.rhs, goal, substitution))
	# 		return subs


	# def BC_AND(self, goal, substitution):
	# 	if substitution == None:
	# 		return

	# 	elif len(goals) == 0:
	# 		return substitution

	# 	else:
	# 		first, rest = self.prioritize_goals(goals)
	# 		subs = self.BC_OR(self.substitute(substitution,first), substitution)
	# 		for sub in subs:
	# 			return self.BC_AND(rest, sub)

	# def initialize_KB(self):
		# self.knowledge_base[Predicates.ADJ_MINE] = [Rule(lhs=[Adj((V.I, V.J), (V.K, V.L)), Mine((V.I, V.J))], rhs=AdjMine((V.I, V.J), (V.K, V.L)))]

		# Rule(lhs=[equals(V.I, V.K), equals(V.J, V.L - 1)]

if __name__ == '__main__':
	agent = KBA(4)
	agent.get_action()
