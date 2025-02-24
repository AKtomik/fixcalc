from operators import operators
from members import Member, valid_none, valid_numbers


from dep.pile import Pile
from dep.file import File


class postFix:
	def __init__(self, expressionString=None):
		if (expressionString):
			self.pile=infixToPostfix(stringToInfix(expressionString))
		else:
			self.pile=Pile()
	
	def calculate(self) -> float:
		return calculatePostfixed(self.pile)

#converter
def stringToInfix(string):
	infix=Pile()

	number=""
	for char in string:

		if char in valid_none:
			#is nothing
			continue

		if char in valid_numbers:
			#is a digit
			#create the number
			#(a number is composed of one or more digits)
			number=number+char
			continue

		#is an operator
		if len(number)>0:
			#add the full number
			infix.empiler(float(number))
			number=""
		
		#add the operator
		infix.empiler(char)
		
	if len(number)>0:
		#add the full number
		infix.empiler(float(number))

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
					
		elif (typeof==int or typeof==float):
			postfix.empiler(op)
		else:
			raise Exception(f"type [{typeof}] de [{op}] non pris en charge")
			
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
		elif (typeof==int or typeof==float):
			cache.empiler(op)
		else:
			raise Exception(f"type [{typeof}] de [{op}] non pris en charge")
	return cache.depiler()