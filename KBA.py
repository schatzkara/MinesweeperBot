import random
from Predicates import *


class KBA:
	def __init__(self, size):
		self.board_size = size
		self.knowledge_base = {}
		self.rules = []

	def get_action(self):
		return (random.rand_int(self.size), random.rand_int(self.size))

	def tell(self, row, col, number):
		if number == 0:
			self.add_to_KB(Predicates.ZERO, Zero((row,col)))

		elif number == 1:
			self.add_to_KB(Predicates.ONE, One((row,col)))

		elif number == 2:
			self.add_to_KB(Predicates.TWO, Two((row,col)))

		elif number == 3:
			self.add_to_KB(Predicates.THREE, Three((row,col)))

	
	def add_to_KB(self, predicate, sentence):
		if predicate not in self.knowledge_base.keys():
			self.knowledge_base[predicate] = []

		self.knowledge_base[predicate].append(sentence)
	

	def substitute(self, substitutions, sentence):


	def unify(self, substitutions, sentence):
		return None

	def standardize_variables(self, sentence):

'''
	def forward_chaining(self, goal):
		first_iteration = true
		while first_iteration or len(new) == 0:
			new = {}
			for r in self.rules:
				r = standardize_variables(r)
				for 
'''

	def fetch_rules(self, goal):


	def prioritize_goals(self, goals):


	def BC_OR(self, goal, substitution):
		rules = self.fetch_rules(goal)
		for r in rules:
			r = standardize_variables(r)

			subs = self.BC_AND(r.lhs, self.unify(r.rhs, goal, substitution))
			return subs


	def BC_AND(self, goal, substitution):
		if substitution == None:
			return

		elif len(goals) == 0:
			return substitution

		else:
			first, rest = self.prioritize_goals(goals)
			subs = self.BC_OR(self.substitute(substitution,first), substitution)
			for sub in subs:
				return self.BC_AND(rest, sub)
