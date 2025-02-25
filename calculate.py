from fixClass import postFix

def calcul(string):
    return f"{postFix(string).calculate()}"
t=calcul("(33*9)/(11*27)+1")
