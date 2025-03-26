# in this file : Differents Results class. Basicily the class that store the result.

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


class Result:
	pass


class RoundResult(Result):

	def __init__(self, floater : float):
		self.float : float=floater
	
	def create_from_float(from_float):
		return RoundResult(from_float)
		
	def create_from_string(the_string):
		return RoundResult(float(the_string))

	def to_float(self):
		if (int(self.float)==self.float):
			return int(self.float)
		return self.float
	
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
	
	def __pow__(self, other):
		self.float=self.float**other.float
		return self
	
	def __str__(self):
		return str(self.to_float())
		

class FractionResult(Result):

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
	
	def to_float(self):
		return self.numerator/self.denominator
	

	def is_one(self):
		return self.numerator==1 and self.denominator==1

	def is_zero(self):
		return self.numerator==0
	
	def is_positive(self):
		return self.numerator*self.denominator>0
	
	
	def __add__(self, other):
		return FractionResult(self.numerator*other.denominator+other.numerator*self.denominator, other.denominator*self.denominator)
		
	def __sub__(self, other):
		return FractionResult(self.numerator*other.denominator-other.numerator*self.denominator, other.denominator*self.denominator)
		
	def __mul__(self, other):
		return FractionResult(self.numerator*other.numerator, self.denominator*other.denominator)
		
	def __truediv__(self, other):
		return FractionResult(self.numerator*other.denominator, self.denominator*other.numerator)

	def __pow__(self, other):
		if (not other.denominator==1):
			raise ValueError("Cant have non-integer in power using fraction result. Switch to decimal.")
		return FractionResult(self.numerator**other.numerator, self.denominator**other.numerator)
	
	def __str__(self):
		self.simplify()
		if (self.denominator==1):
			return str(self.numerator)
		sign=""
		if not self.is_positive():
			sign="-"
		return sign+"("+str(abs(self.numerator)) +"/"+ str(self.denominator)+")"

	#mutate
	def simplify(self):
		if (self.numerator==0):
			self.denominator=1
			return
		a,b=self.numerator, self.denominator
		if (b>a):
			a,b=b,a
		#print("simplify:",a,b)
		david=pgcd(a,b)
		self.numerator=int(self.numerator//david)
		self.denominator=int(self.denominator//david)

		if (self.denominator<0):
			self.numerator=self.numerator*-1
			self.denominator=self.denominator*-1




# pair up an amount and units. (eg: "1", "2x", "4xx", "72xy")
class UnitResultElement:
	# have to be used only by UnitsResult

	def __init__(self, amount, units : dict = {}):
		# check : has to be Sett.result_type_class
		if (not (type(amount) is Sett.result_type_class)):
			raise TypeError(f"amount must be type {Sett.result_type_class} but is {type(amount)}")
		# init
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
		return UnitResultElement(Sett.result_type_class.create_from_float(from_float))
		
	def create_from_string(the_string):
		return UnitResultElement(Sett.result_type_class.create_from_string(the_string))
	
	#mutate
	def __neg__(self):
		self.amount*=Sett.result_type_class(-1)
		return self
	
	#operation
	# here operation are between element, and used by ONLY UnitsReslut
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
	
	def __pow__(self, other):
		result=self.copy()
		result.amount=result.amount**other.amount
		if (not other.units=={}):
			raise ValueError("Cant do power with units. Remove x and other variables from power.")
		for k in self.units.keys():
			result.units[k]=result.units[k]*other.amount.to_float()
		return result

	#print
	def __str__(self):
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
	
	#mutate
	def derivate(self):#mutable
		deriv_count=0
		for k in self.units.keys():
			if (k in Sett.result_derivate_by):
				deriv_count+=1
				#derivate unit 
				# ==
				self.amount*=Sett.result_type_class.create_from_float(self.units[k])#toedit
				self.units[k]-=1
				# ==
		self.simplify()

		if (deriv_count==0):
			self.amount=0
			self.units={}
		return self
		
	def simplify(self):#mutable
		todel=[]
		for k in self.units.keys():
				if (float(self.units[k])==int(self.units[k])):
					self.units[k]=int(self.units[k])
				if (self.units[k]==0):
					todel.append(k)
		for k in todel:
			del self.units[k]
		return self

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
	"-":"⁻",
	".":"˙",
}

#pair up multiples amount and units. (eg: ["1", "2x", "4xx"], ["72xy"])
class UnitsResult(Result):

	def __init__(self, composes : list = []):
		self.compose=composes
	
	def copy(self):
		new_compose=[]
		for element in self.compose:
			new_compose.append(element.copy())
		return UnitsResult(new_compose)
	
	def create_from_float(from_float):
		return UnitsResult([UnitResultElement(Sett.result_type_class.create_from_float(from_float))])
		
	def create_from_string(the_string):
		return UnitsResult([UnitResultElement(Sett.result_type_class.create_from_string(the_string))])
	
	def create_as_unit(the_string):
		return UnitsResult([UnitResultElement(Sett.result_type_class.create_from_float(1), {the_string: 1})])
	
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
		new=self.copy()
		for other_element in other.compose:
			new.add_element(other_element)
		return new
	
	def __sub__(self, other):
		new=self.copy()
		for other_element in other.compose:
			new.add_element(-other_element)
		return new
		
	def __mul__(self, other):
		new_one=UnitsResult()
		new_one.compose=[]#idk why but this is NEEDED. else this is static.
		for i in range(len(self.compose)):
			element_self=self.compose[i]
			for j in range(len(other.compose)):
				element_other=other.compose[j]
				result=element_self*element_other
				new_one.add_element(result)
		return new_one
		
	def __truediv__(self, other):
		new_one=UnitsResult()
		new_one.compose=[]#idk why but this is NEEDED. else this is static.
		if (len(other.compose)>1):
			raise ValueError("Cant divide with more than one term. Keep only one variable in the divider.")
		element_other=other.compose[0]
		for element_self in self.compose:
			result=element_self/element_other
			new_one.add_element(result)
		return new_one
	
	def __pow__(self, other):
		new_one=UnitsResult()
		new_one.compose=[]#idk why but this is NEEDED. else this is static.
		if (len(other.compose)>1):
			raise ValueError("Cant power with more than one term. Keep only one term in the power.")
		element_other=other.compose[0]
		for element_self in self.compose:
			result=element_self**element_other
			new_one.add_element(result)
		return new_one
	
	def __str__(self):
		r=""
		self.simplify()
		if len(self.compose)==0:
			return '0'
		for element in self.compose:
			r+=str(element)
		return r.lstrip('+')
	
	#mutate
	def derivate(self):#mutable
		for element in self.compose:
			element.derivate()
		self.simplify()
		return self
	
	def simplify(self):#mutable
		for element in self.compose:
			if (element.amount==0):
				self.compose.remove(element)
			element.simplify()
		return self
	


class Sett:
	#static

	result_type_class = UnitsResult
	def set_type_class(className):
		Sett.result_type_class = className

	result_build_class=UnitsResult
	#def set_build_class(className):
	#	Sett.result_type_class = className
		
	result_use_unit = True
	def set_use_unit(yesOrNo):
		Sett.result_use_unit = yesOrNo
		if (yesOrNo):
			Sett.result_build_class=UnitsResult
		else:
			Sett.result_build_class=Sett.result_type_class
			

	result_derivate_by = "xyztXYZT"
	def set_derivate_by(all_units_str):
		Sett.result_derivate_by  = all_units_str
		
	convert_const = True
	def set_convert_const(yesOrNoLikeABool):
		Sett.convert_const  = yesOrNoLikeABool