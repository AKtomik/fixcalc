# in this file : PostFix class and fix convertions/operations.

from operators import operators, derivates
from members import MemberType, valid_none, valid_numbers, valid_operators, valid_parentheses, parentheses_closing
from resluts import Sett, Result
from replace import express_engine

from dep.pile import Pile
#from dep.file import File


class PostFix:
	def __init__(self, expression = None):
		#convert
		self.pile=None
		#print(isinstance(expression,str), type(expression),str)
		if expression is None:
			self.pile=Pile()
		elif isinstance(expression,str):
			expression=express_engine(expression)
			print(expression)
			self.pile=infixToPostfix(stringToInfix(expression))
		elif isinstance(expression,PostFix):
			self.pile=expression.pile
		elif isinstance(expression,Result):
			self.pile=Pile().empiler(expression)
		else:
			raise TypeError(f"PostFix expression must by str or Result or PostFix but is {type(expression)}")
	
	def calculate(self) -> float:
		return calculatePostfixed(self.pile)
	
	def derivate(self) -> float:
		return derivatePostfixed(self.pile)

#converter
def stringToInfix(string):

	resultTypeClass=Sett.result_build_class
	#if (Sett.result_use_unit):
	#	resultTypeClass=UnitsResult

	infix=Pile()
	
	#unit=""
	#def unit_exit():
	#	if len(unit)>0:#exit unit
	#		#add the full unit
	#		infix.empiler(resultTypeClass.create_from_string(number))
	#		number=""
	number=""
	last_was=MemberType.NOTHING
	last_closing=False

	for char in string:

		#is nothing
		if char in valid_none:
			pass


		#is a digit
		elif char in valid_numbers:
			
			#smart multiplication
			if (last_was==MemberType.UNIT 
			 		or (last_was==MemberType.PARENTHESE and last_closing)):
				infix.empiler('*')
			last_was=MemberType.NUMBER_FLOAT

			#create the number
			#(a number is composed of one or more digits)
			number=number+char

		#is a parenthes
		elif char in valid_parentheses:
			#exit number check
			if len(number)>0:
				infix.empiler(resultTypeClass.create_from_string(number))
				number=""
				
			closing=(char in parentheses_closing)
			#smart multiplication
			if ((last_closing and last_was==MemberType.PARENTHESE) or not closing and (last_was==MemberType.NUMBER_FLOAT or last_was==MemberType.UNIT)):
				infix.empiler('*')
			last_was=MemberType.PARENTHESE
			last_closing=(closing)

			#add the operator
			infix.empiler(char)

		#is an operator
		elif char in valid_operators:
			#exit number check
			if len(number)>0:
				infix.empiler(resultTypeClass.create_from_string(number))
				number=""
		
			last_was=MemberType.OPERATOR

			#add the operator
			infix.empiler(char)

		#else mean it is an unit
		else:
			#exit number check
			if len(number)>0:
				infix.empiler(resultTypeClass.create_from_string(number))
				number=""
			
			#smart multiplication
			if (last_was==MemberType.UNIT 
			 		or last_was==MemberType.NUMBER_FLOAT 
					or (last_was==MemberType.PARENTHESE and last_closing)):
				infix.empiler('*')
			last_was=MemberType.UNIT

			#add the unit
			infix.empiler(resultTypeClass.create_as_unit(char))


	#exit number check
	if len(number)>0:
		infix.empiler(resultTypeClass.create_from_string(number))
		number=""

	#return it
	r=Pile()
	while (not infix.est_vide()):
		r.empiler(infix.depiler())

	return r


def infixToPostfix(infix):
	#print("infix=",infix)
	cache=Pile()#p
	postfix=Pile()#T'
	while not infix.est_vide():
		op=infix.depiler()

		typeof=type(op)
		
		if (typeof==str):
			match (op):
				
				case '(':
					cache.empiler('(')
					
				case ')':
					dep=cache.depiler()
					while dep!='(':#cache.est_vide() cant be true
						postfix.empiler(dep)
						dep=cache.depiler()

				case _:
					if (not cache.est_vide()):
						while (not cache.est_vide()):
							dep=cache.depiler()
							if (not operators[dep].is_parenthese() and operators[dep].get_strength()>=operators[op].get_strength()):
								postfix.empiler(dep)
							else:
								cache.empiler(dep)
								break
					cache.empiler(op)
					#raise Exception(f"opération [{op}] inconnue")
					
		#elif (typeof==int or typeof==float):
		#	postfix.empiler(op)
		#else:
		#	raise Exception(f"type [{typeof}] de [{op}] non pris en charge")
		else:
			postfix.empiler(op)
			
	while (not cache.est_vide()):
		postfix.empiler(cache.depiler())
		
	r=Pile()
	while (not postfix.est_vide()):
		r.empiler(postfix.depiler())
		
	return r


#computer
def calculatePostfixed(postfix):
	#print("postfix=",postfix)
	cache=Pile()
	while not postfix.est_vide():
		op=postfix.depiler()
		typeof=type(op)
		if (typeof==str):
			last_2=cache.depiler()
			last_1=cache.depiler()
			operatorHere=operators.get(op)
			if (operatorHere==None):
				raise Exception(f"opération [{op}] inconnue")
			else:
				cache.empiler(operatorHere.operate(last_1,last_2))
		#elif (typeof==int or typeof==float):
		#	cache.empiler(op)
		#else:
		#	raise Exception(f"type [{typeof}] de [{op}] non pris en charge")
		else:
			cache.empiler(op)
	return cache.depiler()


#computer
def derivatePostfixed(postfix):
	#result=calculatePostfixed(postfix)
	#result.derivate()
	#return result

	#print("postfix=",postfix)
	cache=Pile()#pile of tuple (normal, derivate)
	while not postfix.est_vide():
		op=postfix.depiler()
		typeof=type(op)
		if (typeof==str):
			last_2=cache.depiler()
			last_1=cache.depiler()
			operatorVanilla=operators.get(op)
			operatorDerivate=derivates.get(op)
			if (operatorVanilla==None or operatorDerivate==None):
				raise Exception(f"opération [{op}] inconnue")
			else:
				#print("depiled both:", last_1[0], last_2[0], last_1[1], last_2[1])
				cache.empiler([operatorVanilla.operate(last_1[0], last_2[0]), operatorDerivate.derivate(last_1[0], last_2[0], last_1[1], last_2[1])])

		else:
			result=[op, op.copy().derivate()]
			#print("repiled both:", result[0], result[1])
			cache.empiler(result)
	return cache.depiler()[1]