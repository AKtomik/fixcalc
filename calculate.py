from fixClass import postFix
from resluts import FractionResult


def calcul(string):
    return f"{postFix(string).calculate()}"
t=calcul("(33*9)/(11*27)+1")

print(FractionResult(1,2))
print(FractionResult(2,20))
print(FractionResult.create_from_float(.5))
print(FractionResult.create_from_string(".12"))