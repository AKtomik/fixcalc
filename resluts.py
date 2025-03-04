#from math import pgcd

def pgcd(greater, lesser):
	if (greater%lesser==0):
		return lesser
	return pgcd(lesser,greater%lesser)


def float_to_scientific_int(x):
	sci_str = "{:e}".format(x)
	mantissa, exponent = sci_str.split("e")
	mantissa_int = int(float(mantissa) * 10**6)
	return mantissa_int, int(exponent) - 6
	
def clean_mantissa_string(string):
	string=string.replace(".","")
	#string=string.replace(".","")
	return int(string)

class FractionResult:

	def __init__(self, numerator : int, denominator : int=1):
		self.numerator : int=numerator
		self.denominator : int=denominator
		self.simplify()
	
	def create_from_float(from_float):
		mantissa_int, exponent = float_to_scientific_int(from_float)
		#exponent*=-1
		if (exponent<0):
			return FractionResult(from_float)
		else:
			return FractionResult(int(mantissa_int*10**exponent),10**exponent)
		
	def create_from_string(the_string):
		return FractionResult(int(the_string.replace(".","")), 10**(len(the_string)-the_string.index(".")-1))

	
	def simplify(self):
		a,b=self.numerator, self.denominator
		if (b>a):
			a,b=b,a
		#print("simplify:",a,b)
		david=pgcd(a,b)
		self.numerator=int(self.numerator//david)
		self.denominator=int(self.denominator//david)
	
	def __add__(self, other):
		return FractionResult(self.numerator*other.denominator+other.numerator*self.denominator, other.denominator*self.denominator)
		
	def __sub__(self, other):
		return FractionResult(self.numerator*other.denominator-other.numerator*self.denominator, other.denominator*self.denominator)
		
	def __mul__(self, other):
		return FractionResult(self.numerator*other.numerator, self.denominator*other.denominator)
		
	def __truediv__(self, other):
		return FractionResult(self.numerator*other.denominator, self.denominator*other.numerator)
	
	def __str__(self):
		self.simplify()
		if (self.denominator==1):
			return str(self.numerator)
		return str(self.numerator) +"/"+ str(self.denominator)
		