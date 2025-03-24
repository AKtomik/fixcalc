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


class RoundResult:

	def __init__(self, floater : float):
		self.float : float=floater
	
	def create_from_float(from_float):
		return RoundResult(from_float)
		
	def create_from_string(the_string):
		return RoundResult(float(the_string))
	
	def __add__(self, other):
		self.float=self.float+other.float
		return self
		
	def __sub__(self, other):
		self.float=self.float-other.float
		return self

	def __mul__(self, other):
		self.float=self.float*other.float
		return self
		
	def __truediv__(self, other):
		self.float=self.float/other.float
		return self
	
	def __str__(self):
		return str(self.float)
		

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
		if ("." in the_string):
			denom=10**(len(the_string)-the_string.index(".")-1)
		else:
			denom=1
		return FractionResult(int(the_string.replace(".","")), denom)

	def is_one(self):
		return self.numerator==1 and self.denominator==1

	def is_zero(self):
		return self.numerator==0
	
	def is_positive(self):
		return self.numerator*self.denominator>0
	
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


class RoundResult:

	def __init__(self, floater : float):
		self.float : float=floater
	
	def create_from_float(from_float):
		return RoundResult(from_float)
		
	def create_from_string(the_string):
		return RoundResult(float(the_string))
	
	def is_one(self):
		return self.float==1

	def is_zero(self):
		return self.float==0
	
	def is_positive(self):
		return self.float>0
	
	def __add__(self, other):
		self.float=self.float+other.float
		return self
		
	def __sub__(self, other):
		self.float=self.float-other.float
		return self

	def __mul__(self, other):
		self.float=self.float*other.float
		return self
		
	def __truediv__(self, other):
		self.float=self.float/other.float
		return self
	
	def __str__(self):
		return str(self.float)
		

result_unit_base_class = RoundResult


class UnitResultElement:#pair up an amount and units. (eg: "1", "2x", "4xx", "72xy")
	#have to be used only on 

	def __init__(self, amount : RoundResult, units : dict = {}):
		self.amount=amount
		self.units=units
	
	def copy(self):
		return UnitResultElement(self.amount, self.units.copy())

	def if_same_unit_as(self, other):
		if len(self.units.keys())!=len(other.units.keys()):
			return False
		for k in self.units.keys():
			pow_self=self.units[k]
			pow_other=other.units.get(k)
			if (pow_other!=pow_self):
				return False
		return True
	
	def create_from_float(from_float):
		return UnitResultElement(result_unit_base_class.create_from_float(from_float))
		
	def create_from_string(the_string):
		return UnitResultElement(result_unit_base_class.create_from_string(the_string))
	
	#mutate
	def __neg__(self):
		self.amount*=-1
		return self
	
	#operation
	#operation are between element, and used by ONLY UnitsReslut
	def __mul__(self, other):
		result=self.copy()
		result.amount*=other.amount
		for k in other.units.keys():
			existing_pow=result.units.get(k)
			if (existing_pow==None):
				existing_pow=0
			result.units[k]=existing_pow+other.units[k]
		return result
		
	def __truediv__(self, other):
		result=self.copy()
		result.amount/=other.amount
		for k in other.units.keys():
			existing_pow=result.units.get(k)
			if (existing_pow==None):
				existing_pow=0
			result.units[k]=existing_pow-other.units[k]
		return result

	#print
	def __str__(self):
	#def printable(self):
		r=""
		#show_amount=True
		show_amount=not (self.amount.is_one() and self.units!={})

		# display sign
		if (self.amount.is_positive() or self.amount.is_zero()):
			r+="+"
		elif (not show_amount):
			r+="-"

		# display amount
		if (show_amount):
			r+=str(self.amount)

		# display units
		for k in self.units.keys():
			r+=k
			pow=str(self.units[k])
			if (pow!="1"):
				for digit in pow:
					r+=digits_to_pow[digit]
		return r

digits_to_pow = {
	"0":"⁰",
	"1":"¹",
	"2":"²",
	"3":"³",
	"4":"⁴",
	"5":"⁵",
	"6":"⁶",
	"7":"⁷",
	"8":"⁸",
	"9":"⁹",
}

class UnitsResult:#pair up multiples amount and units. (eg: ["1", "2x", "4xx"], ["72xy"])

	def __init__(self, composes : list = []):
		self.compose=composes
	
	#def copy(self):
	#	return U
	
	def create_from_float(from_float):
		return UnitsResult([UnitResultElement(result_unit_base_class.create_from_float(from_float))])
		
	def create_from_string(the_string):
		return UnitsResult([UnitResultElement(result_unit_base_class.create_from_string(the_string))])
	
	def create_as_unit(the_string):
		return UnitsResult([UnitResultElement(result_unit_base_class.create_from_float(1), {the_string: 1})])
	
	#usefull
	def add_element(self, added_element):#mutate
		for element in self.compose:
			if element.if_same_unit_as(added_element):
				element.amount+=added_element.amount
				return True
		self.compose.append(added_element)
		return False
	
	def merge_all(self):#'mutate'
		new_one=UnitsResult()
		for element in self.compose:
			new_one.add_element(element)
		self=new_one

	
	#operations
	def __add__(self, other):
		for other_element in other.compose:
			self.add_element(other_element)
		return self
	
	def __sub__(self, other):
		for other_element in other.compose:
			self.add_element(-other_element)
		return self
		
	def __mul__(self, other):
		new_one=UnitsResult()
		new_one.compose=[]#idk why but this is NEEDED. else this is static.
		for i in range(len(self.compose)):
			element_self=self.compose[i]
			for j in range(i, len(other.compose)):
				element_other=other.compose[j]
				result=element_self*element_other
				new_one.add_element(result)
		return new_one
		
	def __truediv__(self, other):
		new_one=UnitsResult()
		if (len(other.compose)>1):
			raise ValueError("cant divide with more than one term (yet)")
		element_other=other.compose[0]
		for element_self in self.compose:
			result=element_self/element_other
			new_one.add_element(result)
		return new_one
	
	def __str__(self):
		r=""
		for element in self.compose:
			r+=str(element)
		return '['+r.lstrip('+')+']'