# in this file : Differents operators and Operator class. Interactions between result.
from enum import Enum
from resluts import Sett

class OperatorType(Enum):

	DUAL_COMPUTE = 1
	#takes 2 arguments and return 1 result

	SIGNLE_COMPUTE = 2
	#takes 1 argument and return 1 result

	PARENTHESES = 3
	#just for odering

class Operator:
	def __init__(self, theType, lambdaAction, strength=1):
		self.type=theType
		self.action=lambdaAction#have to takes two arguments
		self.strength=strength
	
	def operate(self, a, b):
		return self.action(a,b)
	
	def transformate(self, a):
		return self.action(a)
    
	def derivate(self, a, b, da, db):
		return self.action(a, b, da, db)
	
	def get_strength(self):
		"""
		the strength define the priority of the operation.
		the greater strength go first.
		if same strength, defined by string order.
		"""
		return self.strength
	
	def get_type(self):
		return self.type
	
	def is_parenthese(self):
		return self.type==OperatorType.PARENTHESES

operators = {
	'+': Operator(OperatorType.DUAL_COMPUTE, lambda a, b : a+b, 1),
	'-': Operator(OperatorType.DUAL_COMPUTE, lambda a, b : a-b, 1),
	'*': Operator(OperatorType.DUAL_COMPUTE, lambda a, b : a*b, 2),
	'/': Operator(OperatorType.DUAL_COMPUTE, lambda a, b : a/b, 2),
	'^': Operator(OperatorType.DUAL_COMPUTE, lambda a, b : a**b, 3),
	'(': Operator(OperatorType.PARENTHESES, None, 10),#special operator.
	')': Operator(OperatorType.PARENTHESES, None, 10),#special operator.
	'_': Operator(OperatorType.SIGNLE_COMPUTE, lambda a : -a, 4),
}
derivates = {
    '+': Operator(OperatorType.DUAL_COMPUTE, lambda a, b, da, db : da+db),
    '-': Operator(OperatorType.DUAL_COMPUTE, lambda a, b, da, db : da-db),
    '*': Operator(OperatorType.DUAL_COMPUTE, lambda a, b, da, db : da*b+db*a),
    '/': Operator(OperatorType.DUAL_COMPUTE, lambda a, b, da, db : (da*b-db*a)/(b)**Sett.result_build_class.create_from_float(2)),
    '^': Operator(OperatorType.DUAL_COMPUTE, lambda a, b, da, db : b*(a**(b - Sett.result_build_class.create_from_float(1)))*da)
}