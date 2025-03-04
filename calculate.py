from fixClass import postFix
from resluts import FractionResult


def calcul(string, resultTypeClass):
    return f"{postFix(string, resultTypeClass).calculate()}"

print(FractionResult(1,2))
print(FractionResult(2,20))
print(FractionResult.create_from_float(.5))
print(FractionResult.create_from_string(".12"))