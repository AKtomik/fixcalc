from fixClass import postFix
from resluts import FractionResult, RoundResult, UnitsResult


def calcul(string, resultTypeClass=RoundResult):
    return f"{postFix(string, resultTypeClass, True).calculate()}"

def derive(string, resultTypeClass=RoundResult):
    return f"{postFix(string, resultTypeClass, True).derivate()}"
#t=calcul("(33*9)/(11*27)+1")

#print(UnitsResult.create_as_unit("x")+UnitsResult.create_as_unit("y"))
#print(UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("y"))
#print(UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("y"))
#print(UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("y"))
#print(UnitsResult.create_from_string("-5")*(UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("x")))
#print(UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("x")*UnitsResult.create_as_unit("x"))
#print(calcul("1/3", UnitsResult))

#some tests
#print(calcul("(33*9)/(11*28)+1", FractionResult))
#print(calcul("13*x*y*y*(13*31)", FractionResult))
#print(calcul("caca", FractionResult))
#print(calcul("19x/18y", FractionResult))
#print(calcul("1/2", FractionResult))
#print(calcul("1-3/2", FractionResult))
#print(calcul("(xvzezx)^2^2.1", RoundResult))
#print(calcul("(18abcd-4bbbd-bbdd-4accc+aadd)/(aaaa)", FractionResult))


print(calcul("X*(X+1)*(X-49)", FractionResult))
print(calcul("(X+1)*(X-49)", FractionResult))
print(calcul("(X^2-48X-49)*X", FractionResult))
#print(calcul("(X+1)(X-49)(X+4012)", FractionResult))
#print(derive("(X+1)(X-49)(X+4012)", FractionResult))


#print(calcul("(33*9)/(11*28)+1", RoundResult))
#print(calcul("(33*9)/(11*28)+1", FractionResult))

#print(FractionResult(1,2))
#print(FractionResult(2,20))
#print(FractionResult.create_from_float(.5))
#print(FractionResult.create_from_string(".12"))