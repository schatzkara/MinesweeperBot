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


	def unify(self, sentence1, sentence2, substitution):
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
	def unify_var(self, variable1, variable2):


	def is_variable(self, sentence):


	def is_compound(self, sentence):


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
