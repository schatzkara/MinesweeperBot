
class Rule:
	self __init__(self, lhs, rhs):
		self.lhs = lhs  # the antecedent as a list of conjuncts or empty list if rhs is an atomic fact
		self.rhs = rhs  # the consequent