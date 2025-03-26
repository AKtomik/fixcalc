# in this file : Some tests use and used.
from fixcalc import *

# tests

print(calcul("(X+2)^10"))
print(calcul("(X+Y+Z)^3"))
print(calcul("(A+B+C+D+E+F)^2"))

#print(calcul("X*(X+1)*(X-49)"))
#print(calcul("(X+1)*(X-49)"))
#print(calcul("(X^2-48X-49)*X"))
#print(calcul("(X+1)(X-49)(A+4012)"))

#print(derive("X*(X+1)*(X-49)"))
#print(derive("(X+1)(X-49)(A+4012)"))

#print(derive("13aX"))
#print(derive(derive("13aX")))
#print(derive(derive("X^3")))
#print(derive(derive("X^10²")))
#print(derive(derive("X^(10²)")))
#print(derive("X⁹⁸"))

# old tests


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

#print(derive(derive("13aX")))


#print(calcul("(33*9)/(11*28)+1", RoundResult))
#print(calcul("(33*9)/(11*28)+1", FractionResult))

#print(FractionResult(1,2))
#print(FractionResult(2,20))
#print(FractionResult.create_from_float(.5))
#print(FractionResult.create_from_string(".12"))

#print(calcul("314+1592-6535/8979*32+38"))
#print(calcul("(33*9)/(11*27)+1"))
#print(calcul("2-1"))
#print(calcul("2/3"))
#print(calcul("3/2"))
#print(calcul("1+2*3"))
#print(calcul("1+(2*3)"))