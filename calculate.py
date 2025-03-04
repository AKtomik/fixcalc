from fixClass import postFix
from resluts import FractionResult, RoundResult


def calcul(string, resultTypeClass=RoundResult):
    return f"{postFix(string, resultTypeClass).calculate()}"
#t=calcul("(33*9)/(11*27)+1")

print(calcul("(33*9)/(11*28)+1", RoundResult))
print(calcul("(33*9)/(11*28)+1", FractionResult))

#print(FractionResult(1,2))
#print(FractionResult(2,20))
#print(FractionResult.create_from_float(.5))
#print(FractionResult.create_from_string(".12"))