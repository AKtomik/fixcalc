# in this file : calcul() and derive() functions. Import theses god functions from here.
from allfix import PostFix
from resluts import Sett, Result, FractionResult, RoundResult


def calcul(expression : str | Result | PostFix) -> PostFix:
    return PostFix(expression).calculate()

def derive(expression : str | Result | PostFix) -> PostFix:
    return PostFix(expression).derivate()


# type of result computer used. FractionResult or RoundResult are valid.
Sett.set_type_class(RoundResult)#FractionResult/RoundResult
# dont change it, is OBLIGATORY for derivate and use variables (like x or y).
Sett.set_use_unit(True)
# by what is it derivated. Generally "xXyYtT" and/or others.
Sett.set_derivate_by("xyztXYZT")